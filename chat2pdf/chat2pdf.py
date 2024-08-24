"""Chat with your pdf.

Name        : chat2pdf.py
Author      : E.Taskesen
Contact     : erdogan.taskesen@minienw.nl
github      : https://github.com/erdogant/chat2pdf
Licence     : See licences

"""

# import subprocess
import streamlit as st
from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

import os
import re
import psutil
import time
import itertools
import sys
import logging

logger = logging.getLogger('')
[logger.removeHandler(handler) for handler in logger.handlers[:]]
console = logging.StreamHandler()
formatter = logging.Formatter('[chat2pdf] >%(levelname)s> %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)
logger = logging.getLogger(__name__)


class chat2pdf():
    """chat2pdf.
    In order to use the LLM locally, we first need to install Ollama on our system.
    Go to the following official site and download the open source platform. The system may need to be restarted afterward.
    https://ollama.com/library/llama3.1

    Once the model has been downloaded, you can communicate with it via the terminal.
    >>> ollama run llama3.1
    >>> ollama pull phi3

    The methods works as following:
    1. The PDF file is uploaded and the text it contains is extracted.
    2. The extracted text is divided into smaller chunks that are stored in a vector store.
    3. The user enters a question.
    4. The question, i.e. the input, is prepared for the model by combining the question and the context.
    5. The LLM is queried and generates the answer.

    In principle, several PDF files can be uploaded at the same time, whereby these together form the context.

    """

    def __init__(self, model='phi3', method='en_core_web_sm', verbose='info'):
        """Initialize chat2pdf with user-defined parameters.

        Parameters
        ----------
        model : String: Name of the model
            'llama3.1'
            'phi3'
        method : String
            'en_core_web_sm'
        verbose : String
            'info'.

        Returns
        -------
        None.

        """
        self.method = method
        # Set the logger
        set_logger(verbose=verbose)
        # Set the prompt
        self.prompt = self.set_prompt()
        # Set Template
        self.template = self.set_template()
        # Model
        self.model = OllamaLLM(model=model)

        # Create spacy embedding
        # self.embeddings = self.create_spacy_embedding(method)
        # Set chunk sizes
        # self.chunk_size = 1000
        # self.chunk_overlap = 200

        if "KMP_DUPLICATE_LIB_OK" not in os.environ:
            # If it doesn't exist, set it to "TRUE"
            os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
            logger.info("Setting [KMP_DUPLICATE_LIB_OK] in environ.")

    def question(self, user_question):
        """Process the user input and calls up the model."""
        # Configure and request
        logger.info(f'Q: {user_question}')
        # Store user question
        self.user_question = user_question
        # Setup chain
        self.create_conversational_chain()
        # Setup chain
        self.get_repsonse(user_question)

    def set_prompt(self):
        """Set prompt."""
        prompt = """
        You are an helpful assistant and your default language is English.
        Your goal is to be concise in your answer but only use the information in the context that is provided.
        However, do make sure your sentences are grammerly correct.
        If the answer is not available in the provided context, state this clearly and do not offer other information.
        """
        return prompt

    def set_template(self):
        """Define the prompt behavior."""
        template = """
        System: {prompt}

        Context: {context}

        Question: {question}

        Answer:
        """
        return template

    def create_conversational_chain(self, show_progress=True):
        # Request to the model
        prompt_template = ChatPromptTemplate.from_template(self.template)
        # Create chain
        self.chain = prompt_template | self.model

    def get_repsonse(self, user_question, show_progress=True):
        """Create the input for the model based on the prompt and context."""
        # Without progressbar response
        if not show_progress:
            full_response = self.chain.invoke({'prompt': self.prompt, "context": self.context, "question": self.user_question})
        else:
            # Setup progressbar
            full_response = ""
            spinner = itertools.cycle(['-', '/', '|', '\\'])

            # Stream the response
            for chunk in self.chain.stream({'prompt': self.prompt, "context": self.context, "question": self.user_question}):
                if isinstance(chunk, str):
                    full_response += chunk
                else:
                    # If chunk is not a string, it might be a dictionary or another object. Adjust this part based on the actual structure of your chunks
                    full_response += str(chunk)

                # Update spinner
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                sys.stdout.write('\b')
                time.sleep(0.01)  # Small delay to control spinner speed

            # Clear the spinner
            sys.stdout.write(' \b')

        # Remove ANSI codes
        full_response = re.sub(r'\x1b\[.*?m', '', full_response)
        # Update context with the new interaction
        self.context += f"\nUser: {self.user_question}\nAI: {full_response}"
        # Store
        self.response = full_response
        # Output response
        logger.info(f"\n{self.response}")

    def create_spacy_embedding(self, method='en_core_web_sm'):
        """Create spacy Embeddings.

        An object for text embeddings, numerical representation of text, using the Spacy model must be created to capture the meaning of the text uploaded as a PDF file.
        The embeddings are then used to vectorize the text in order to store them in a vector store so that they can be used for semantic search.

        """
        return SpacyEmbeddings(model_name=method)


    def create_vectors(self, text_chunks):
        """Create a vector store for the text chunks.

        The "create_vectors()" function uses the aforementioned FAISS to store the embeddings of the text chunks.
        The vector store enables faster retrieval and searching of texts based on the existing embeddings.
        The vector store is saved locally so that it can be accessed later.

        """
        logger.info('Creating embeddings and storing locally [faiss_db]..')
        vector_store = FAISS.from_texts(text_chunks, embedding=self.embeddings)
        # self.context_vectors = vector_store
        # vector_store.save_local("faiss_db")


    def pdf_read(self, pdf_doc):
        """Read the text from PDF document.

        The "pdf_read()" function reads the entire text from a PDF file.
        Specifically, "PyPDF2" is used to extract the text. The text is then combined into a single character string "text", which is returned.
        The function is important in order to make the content of the PDF file available for further processing steps.

        """
        text = ""
        for pdf in pdf_doc:
            logger.info(f'Reading file: {pdf}')
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        self.context = text
        # Create chunks
        # context_chunks = create_text_chunks(text, chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        # Store vector
        # self.create_vectors(context_chunks)


# %%
def create_text_chunks(text, chunk_size=1000, chunk_overlap=200):
    """Create text chunks from a large text block.
    The combined character string from the previous function is split into smaller text chunks in the next step using the "create_text_chunks()"
    The maximum number of characters per chunk "chunk_size" is 1000 and the number of characters that can overlap in adjacent chunks "chunk_overlap" is 200.
    This implementation enables the app to query and process larger amounts of text more efficiently.

    """
    logger.info('Creating chunks..')
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    text_chunks = text_splitter.split_text(text)
    return text_chunks


# %%
def get_logger():
    return logger.getEffectiveLevel()


def set_logger(verbose: [str, int] = 'info'):
    """Set the logger for verbosity messages.

    Parameters
    ----------
    verbose : [str, int], default is 'info' or 20
        Set the verbose messages using string or integer values.
        * [0, 60, None, 'silent', 'off', 'no']: No message.
        * [10, 'debug']: Messages from debug level and higher.
        * [20, 'info']: Messages from info level and higher.
        * [30, 'warning']: Messages from warning level and higher.
        * [50, 'critical']: Messages from critical level and higher.

    Returns
    -------
    None.

    > # Set the logger to warning
    > set_logger(verbose='warning')
    > # Test with different messages
    > logger.debug("Hello debug")
    > logger.info("Hello info")
    > logger.warning("Hello warning")
    > logger.critical("Hello critical")

    """
    # Set 0 and None as no messages.
    if (verbose==0) or (verbose is None):
        verbose=60
    # Convert str to levels
    if isinstance(verbose, str):
        levels = {'silent': 60,
                  'off': 60,
                  'no': 60,
                  'debug': 10,
                  'info': 20,
                  'warning': 30,
                  'error': 50,
                  'critical': 50}
        verbose = levels[verbose]

    # Show examples
    logger.setLevel(verbose)

def disable_tqdm():
    """Set the logger for verbosity messages."""
    return (True if (logger.getEffectiveLevel()>=30) else False)

# %%
def sidebar(model):
    # Upload pdf
    context = ""
    pdf_doc = st.sidebar.file_uploader("Upload PDF Files", accept_multiple_files=True)

    if pdf_doc:
        logger.info(f"Reading pdf..")
        # Read the entire PDF text
        model.pdf_read(pdf_doc)
        # Extract the context
        context = model.context
        st.sidebar.caption(f'Length context: {len(model.context)} characters')

    logger.info(f'Total number of characters in files: {len(context)}')
    return context


    # %%
def main():
    """Main function of the Streamlit application."""
    response = ''

    model_type = st.sidebar.selectbox('Select model', ['Phi3', 'llama3.1'], index=0)
    # Intialize model
    model = chat2pdf(model=model_type)
    # Make sidebar
    pdf_text = sidebar(model)
    # Ask question
    user_question = st.chat_input("Ask a question")

    if user_question and pdf_text:
        with st.spinner(f'Processing question with {model_type}...'):
            # Ask the question to the model
            model.question(user_question)
            response = model.response

        with st.chat_message("human"):
            st.write(f"{user_question}")
        with st.chat_message("ai"):
            st.write(f"{response}")

    elif user_question and not pdf_text:
        with st.chat_message("ai"):
            st.write(f"Upload first your PDF files.")

    # Monitor RAM consumption
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / (1024 ** 2)  # Conversion to megabytes
    st.sidebar.caption(f"Memory usage: {memory_usage:.2f} MB")


# %% Main
if __name__ == "__main__":
    # st.set_page_config(layout="centered", page_title="Chat2pdf", page_icon="🚀")
    main()
