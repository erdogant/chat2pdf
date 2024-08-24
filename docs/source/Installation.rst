Installation
################

Create environment
**********************

If desired, install ``chat2pdf`` from an isolated Python environment using conda:

.. code-block:: python

    conda create -n env_chat2pdf python=3.8
    conda activate env_chat2pdf


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install chat2pdf

    # Force update to latest version
    pip install -U chat2pdf


Github source
************************************

.. code-block:: console

    # Install directly from github
    pip install git+https://github.com/erdogant/chat2pdf


Uninstalling
################

Remove environment
**********************

.. code-block:: console

   # List all the active environments. chat2pdf should be listed.
   conda env list

   # Remove the chat2pdf environment
   conda env remove --name chat2pdf

   # List all the active environments. chat2pdf should be absent.
   conda env list


Remove installation
**********************

Note that the removal of the environment will also remove the ``chat2pdf`` installation.

.. code-block:: console

    # Install from Pypi:
    pip uninstall chat2pdf

