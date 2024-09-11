# %%
# import chat2pdf
# print(dir(chat2pdf))
# print(chat2pdf.__version__)

# %%
# https://ollama.com/library/llama3.1
# https://python.langchain.com/v0.2/docs/integrations/llms/ollama/

# %%
from chat2pdf import chat2pdf
model = chat2pdf()

print(model.prompt)

# Change prompt:
# model.prompt = "Answer with 1 number"

model.context = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.
It is named after the engineer Gustave Eiffel, whose company designed and built the tower.
The tower is 324 meters (1,063 ft) tall, about the same height as an 81-story building, and the tallest structure in Paris.
The number of visitors on yearly basis is 10.000.
"""
print(model.context)

# question = "How many people visit the Eiffel Tower?"
# question = "How width is the Eiffel Tower?"
question = "How tall is the Eiffel Tower?"

# Template
print(model.template)

# Now ask the question
model.question(question)

# Reponse
# print(model.response)


# %%
from chat2pdf import chat2pdf
model = chat2pdf(model='Phi3')
print(model.prompt)

model.pdf_read([r'D:\OneDrive\DILAB\FOW\20230906 MT FOW werving.pdf'])
print(model.context)

question = "Wat is de betekenis van FOW?"
model.question(question)

# print(model.response)

model.question('Wat was mijn eerste vraag?')

# %%
# pip install pypdf
# !pip install langchain_community

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from operator import itemgetter
import os

# PDF
PDF_FILE = r"./notebooks/paul.pdf"
os.path.isfile(PDF_FILE)

# We'll be using Llama 3.1 8B for this example.
MODEL = "llama3.1"

# Loading the PDF document
# Let's start by loading the PDF document and breaking it down into separate pages.
loader = PyPDFLoader(PDF_FILE)
pages = loader.load()

print(f"Number of pages: {len(pages)}")
print(f"Length of a page: {len(pages[1].page_content)}")
# print("Content of a page:", pages[1].page_content)


# Splitting the pages in chunks
# Pages are too long, so let's split pages into different chunks.
splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
chunks = splitter.split_documents(pages)

print(f"Number of chunks: {len(chunks)}")
print(f"Length of a chunk: {len(chunks[1].page_content)}")
print("Content of a chunk:", chunks[1].page_content)


# Storing the chunks in a vector store
# We can now generate embeddings for every chunk and store them in a vector store.
embeddings = OllamaEmbeddings(model=MODEL)
vectorstore = FAISS.from_documents(chunks, embeddings)


# Setting up a retriever
# We can use a retriever to find chunks in the vector store that are similar to a supplied question.
retriever = vectorstore.as_retriever()
retriever.invoke("What can you get away with when you only have a small number of users?")

# Configuring the model
# We'll be using Ollama to load the local model in memory. After creating the model, we can invoke it with a question to get the response back.
model = ChatOllama(model=MODEL, temperature=0)
model.invoke("Who is the president of the United States?")

# Parsing the model's response
# The response from the model is an AIMessage instance containing the answer. We can extract the text answer by using the appropriate output parser. We can connect the model and the parser using a chain.
parser = StrOutputParser()
chain = model | parser
print(chain.invoke("Who is the president of the United States?"))


# Setting up a prompt
# In addition to the question we want to ask, we also want to provide the model with the context from the PDF file. We can use a prompt template to define and reuse the prompt we'll use with the model.
template = """
You are an assistant that provides answers to questions based on
a given context.

Answer the question based on the context. If you can't answer the
question, reply "I don't know".

Be as concise as possible and go straight to the point.

Context: {context}

Question: {question}
"""

prompt = PromptTemplate.from_template(template)
print(prompt.format(context="Here is some context", question="Here is a question"))


# Adding the prompt to the chain
# We can now chain the prompt with the model and the parser.
chain = prompt | model | parser
chain.invoke({
    "context": "Anna's sister is Susan", 
    "question": "Who is Susan's sister?"
})


# Adding the retriever to the chain
# Finally, we can connect the retriever to the chain to get the context from the vector store

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
    }
    | prompt
    | model
    | parser
)

# Using the chain to answer questions
# Finally, we can use the chain to ask questions that will be answered using the PDF document.

questions = [
    "What can you get away with when you only have a small number of users?",
    "What's the most common unscalable thing founders have to do at the start?",
    "What's one of the biggest things inexperienced founders and investors get wrong about startups?",
]

for question in questions:
    print(f"Question: {question}")
    print(f"Answer: {chain.invoke({'question': question})}")
    print("*************************\n")
    