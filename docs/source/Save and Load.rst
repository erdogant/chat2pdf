
Save and Load
''''''''''''''

Saving and loading models is desired as the learning proces of a model for ``chat2pdf`` can take up to hours.
In order to accomplish this, we created two functions: function :func:`chat2pdf.save` and function :func:`chat2pdf.load`
Below we illustrate how to save and load models.


Saving
----------------

Saving a learned model can be done using the function :func:`chat2pdf.save`:

.. code:: python

    import chat2pdf

    # Load example data
    X,y_true = chat2pdf.load_example()

    # Learn model
    model = chat2pdf.fit_transform(X, y_true, pos_label='bad')

    Save model
    status = chat2pdf.save(model, 'learned_model_v1')



Loading
----------------------

Loading a learned model can be done using the function :func:`chat2pdf.load`:

.. code:: python

    import chat2pdf

    # Load model
    model = chat2pdf.load(model, 'learned_model_v1')

