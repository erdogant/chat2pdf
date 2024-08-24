# chat2pdf

[![Python](https://img.shields.io/pypi/pyversions/chat2pdf)](https://img.shields.io/pypi/pyversions/chat2pdf)
[![Pypi](https://img.shields.io/pypi/v/chat2pdf)](https://pypi.org/project/chat2pdf/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/chat2pdf/)
[![LOC](https://sloc.xyz/github/erdogant/chat2pdf/?category=code)](https://github.com/erdogant/chat2pdf/)
[![Downloads](https://static.pepy.tech/personalized-badge/chat2pdf?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/chat2pdf)
[![Downloads](https://static.pepy.tech/personalized-badge/chat2pdf?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/chat2pdf)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/chat2pdf/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/chat2pdf.svg)](https://github.com/erdogant/chat2pdf/network)
[![Issues](https://img.shields.io/github/issues/erdogant/chat2pdf.svg)](https://github.com/erdogant/chat2pdf/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![DOI](https://zenodo.org/badge/228166657.svg)](https://zenodo.org/badge/latestdoi/228166657)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://towardsdatascience.com/what-are-chat2pdf-loadings-and-biplots-9a7897f2e559)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg?logo=github%20sponsors)](https://erdogant.github.io/chat2pdf/pages/html/Documentation.html#colab-notebook)
![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/chat2pdf)
![GitHub repo size](https://img.shields.io/github/repo-size/erdogant/chat2pdf)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://erdogant.github.io/chat2pdf/pages/html/Documentation.html#)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``chat2pdf`` is Python package

# 
**Star this repo if you like it! ⭐️**
#


### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install chat2pdf from PyPI (recommended). chat2pdf is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as follows:

```bash
conda create -n env_chat2pdf python=3.12
conda activate env_chat2pdf
```

```bash
pip install chat2pdf            # normal install
pip install --upgrade chat2pdf # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/erdogant/chat2pdf.git@0.1.0#egg=master
pip install git+https://github.com/erdogant/chat2pdf#egg=master
pip install git+https://github.com/erdogant/chat2pdf

# By cloning
git clone https://github.com/erdogant/chat2pdf.git
cd chat2pdf
pip install -U -e .
```  

#### Import chat2pdf package
```python
from chat2pdf import chat2pdf
```

#### Example by using PDF files
```python

# Import
from chat2pdf import chat2pdf
# Initialize
client = chat2pdf(model='Phi3')

# Check prompt
print(client.prompt)

client.pdf_read([r'C:\my_personal_pdf.pdf'])
print(client.context)

question = "Create a summary with at most 100 words"
client.question(question)

# print(client.response)
client.question('What was my first question?')

```


#### Example by adding alternatively context:
```python

# Import
from chat2pdf import chat2pdf
# Initialize
client = chat2pdf()

# print the prompt text
print(client.prompt)

# Change prompt:
# client.prompt = "Use Dutch as language."

client.context = """
The Eiffel Tower is a wrought iron lattice tower on the Champ de Mars in Paris, France.
It is named after the engineer Gustave Eiffel, whose company designed and built the tower.
The tower is 324 meters (1,063 ft) tall, about the same height as an 81-story building, and the tallest structure in Paris.
The number of visitors on yearly basis is 10.000.
"""
print(client.context)

# question = "How many people visit the Eiffel Tower?"
# question = "How width is the Eiffel Tower?"
question = "How tall is the Eiffel Tower?"

# Template
print(client.template)

# Now ask the question
client.question(question)

# Reponse
# print(client.response)

```

#### Example by adding directly Context:
```Bash

streamlit run chat2pdf.py

```

<p align="center">
  <img src="https://github.com/erdogant/chat2pdf/blob/master/docs/figs/screenshot_gui.png" width="600" />
</p>


#### References
* https://github.com/erdogant/chat2pdf

#### Citation
Please cite in your publications if this is useful for your research (see citation).
   
### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
