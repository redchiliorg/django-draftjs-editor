import os

from django import forms
from django.conf import settings
from django.forms.renderers import DjangoTemplates

from draftjs_editor.forms import EditorField, Editor
from draftjs_editor.test.test_cases import TestCase


class EditorFieldTestCase(TestCase):
    class Form(forms.Form):
        content = EditorField()

    def setUp(self):
        super().setUp()
        self.value = self.create_data_from_text('Hello world!')
        self.form = self.Form({'content': self.value})

    def testFormIsValid(self):
        self.assertTrue(self.form.is_valid())

    def testContentHTMLEqual(self):
        self.form.is_valid()
        content = self.form.cleaned_data['content']
        self.assertContentHTMLEqual(content, '<p>Hello world!</p>')


class EditorSnapshotTestCase(TestCase):
    renderer = DjangoTemplates()
    name = 'content'
    widget = Editor()
    snapshots_path = os.path.join(
        os.path.dirname(__file__), 'snapshots', 'editor.html'
    )

    def setUp(self):
        super().setUp()
        self.value = self.create_data_from_text('Hello world!')
        self.rendered = self.widget.render(
            self.name, self.value, None, self.renderer
        )

        if settings.DRAFTJS_EDITOR_UPDATE_SNAPSHOTS:
            self.write_snapshot(self.rendered)

        self.snapshot = self.read_snapshot()

    def write_snapshot(self, output):
        open(self.snapshots_path, 'w').write(output)

    def read_snapshot(self):
        return open(self.snapshots_path, 'r').read()

    def testRendered(self):
        self.assertHTMLEqual(self.rendered, self.snapshot)
