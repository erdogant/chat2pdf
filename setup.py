import setuptools
import re
# import subprocess

# versioning ------------
VERSIONFILE = "chat2pdf/__init__.py"
getversion = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


# def install_spacy_model():
    # subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_sm"])

# Setup ------------
with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()
setuptools.setup(
     install_requires=['streamlit', 'PyPDF2', 'langchain', 'langchain-community', 'langchain_ollama'],
     python_requires='>=3',
     name='chat2pdf',
     version=new_version,
     author="Erdogan Taskesen",
     author_email="erdogant@gmail.com",
     description="Python package chat2pdf",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/erdogant/chat2pdf",
	 download_url = 'https://github.com/erdogant/chat2pdf/archive/' + new_version + '.tar.gz',
     packages=setuptools.find_packages(), # Searches throughout all dirs for files to include
     include_package_data=True, # Must be true to include files depicted in MANIFEST.in
     license_files=["LICENSE"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     # cmdclass={'install': install_spacy_model},
 )
