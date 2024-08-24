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





<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``chat2pdf`` is Python package

# 
**Star this repo if you like it! ⭐️**
#


## Blog/Documentation

* [**chat2pdf documentation pages (Sphinx)**](https://erdogant.github.io/chat2pdf/)
* [**Notebook with examples**](https://colab.research.google.com/github/erdogant/chat2pdf/blob/master/notebooks/chat2pdf.ipynb)
* [**Read more details and usage about chat2pdf in this blog!**](https://towardsdatascience.com/chat2pdf)

* <a href="https://erdogant.github.io/chat2pdf/"> <img src="https://img.shields.io/badge/Sphinx-Docs-Green" alt="Open documentation pages"/> </a> chat2pdf documentation pages 
* <a href="https://colab.research.google.com/github/erdogant/chat2pdf/blob/master/notebooks/chat2pdf.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open example In Colab"/> </a> Notebook example 
* <a href="https://towardsdatascience.com/a-step-by-step-guide-for-clustering-images-4b45f9906128"> <img src="https://img.shields.io/badge/Medium-Blog-blue" alt="Open Blog"/> </a> Blog: A step-by-step guide for clustering images 


### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install chat2pdf from PyPI (recommended). chat2pdf is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_chat2pdf python=3.8
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
pip install -U .
```  

#### Import chat2pdf package
```python
import chat2pdf as chat2pdf
```

#### Example:
```python
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/chat2pdf/data/example_data.csv')
model = chat2pdf.fit(df)
G = chat2pdf.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/chat2pdf/blob/master/docs/figs/fig1.png" width="600" />
  
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
