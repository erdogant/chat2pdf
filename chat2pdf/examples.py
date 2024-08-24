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
