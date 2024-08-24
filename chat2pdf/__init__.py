from chat2pdf.chat2pdf import chat2pdf


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.0'

# module level doc-string
__doc__ = """
chat2pdf
=====================================================================

Description
-----------
This package can answer questions related to one or multiple PDF files. It runs entirely locally and various models can be choosen using Ollama.
This package also includes a user interface where pdf files can be selected and questions asked.

Examples
--------
>>> # Example reading PDF files and ask questions.
>>> #
>>> # Import library
>>> from chat2pdf import chat2pdf
>>> # Initialize
>>> client = chat2pdf(model='Phi3')
>>> #
>>> # Check prompt
>>> print(client.prompt)
>>> #
>>> client.pdf_read([r'C:\my_personal_file.pdf'])
>>> print(client.context)
>>> #
>>> question = "Create a summary with at most 100 words"
>>> client.question(question)
>>> #
>>> # print(client.response)
>>> client.question('What was my first question?')

Examples
--------
>>> # Example by providing alternative context and then ask questions.
>>> # Import
>>> from chat2pdf import chat2pdf
>>> # Initialize
>>> client = chat2pdf()
>>> #
>>> # print the prompt text
>>> print(client.prompt)
>>> #
>>> # Change prompt:
>>> # client.prompt = "Use Dutch as language."
>>> #
>>> client.context = "The Eiffel Tower is a wrought iron lattice tower on the Champ de Mars in Paris, France.  It is named after the engineer Gustave Eiffel, whose company designed and built the tower. The tower is 324 meters (1,063 ft) tall, about the same height as an 81-story building, and the tallest structure in Paris. The number of visitors on yearly basis is 10.000."
>>> print(client.context)
>>> #
>>> # question = "How many people visit the Eiffel Tower?"
>>> # question = "How width is the Eiffel Tower?"
>>> question = "How tall is the Eiffel Tower?"
>>> #
>>> # Template
>>> print(client.template)
>>> #
>>> # Now ask the question
>>> client.question(question)
>>> #
>>> # Reponse
>>> # print(client.response)
>>> #

Examples
--------
>>> # Run GUI
>>> streamlit run chat2pdf.py

"""
