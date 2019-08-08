""""""""""""""""""""""""
Django Draft.js Editor
""""""""""""""""""""""""
..................................................
Draft.js rich text editor extension for Django
..................................................

`Draft.js <https://github.com/facebook/draft-js>`_
is a JavaScript rich text editor framework maintained by
`Facebook team <https://github.com/facebook>`_.

.. contents:: Contents

=========================
Installation
=========================
.. code-block:: bash

    pip install git+https://github.com/mi6gan/django-draftjs-editor

===================
Usage
===================
------------------------
Text model field
------------------------

.. code-block:: python

    from django.db import models
    from draftjs_editor.fields import EditorTextField

    class Model(models.Model):
        editor = EditorTextField()

-----------------------------
Postgres JSON model field
-----------------------------

.. code-block:: python

    from django.db import models
    from draftjs_editor.fields import EditorJSONField

    class Model(models.Model):
        editor = EditorJSONField()

------------------------
Form field
------------------------
``EditorField`` is a default ``formfield`` for editor model fields.
But you may need to add it explicitly in a form:

.. code-block:: python

    from django import forms
    from draftjs_editor.forms import EditorField

    class Form(forms.Form):
        editor = EditorField()

------------------------
Form widget
------------------------
``Editor`` is just another django form widget and can be
easily used at field initialization:

.. code-block:: python

    from django import forms
    from draftjs_editor.forms import Editor

    class Form(forms.Form):
        editor = forms.TextField(widget=Editor)



===================
Advanced usage
===================
We are going to improve our documentation.
Just after covering the code with tests for basic use cases.
