from draftjs_editor.fields import EditorJSONField
from draftjs_editor.test.test_cases import TestCase
from draftjs_editor.forms import EditorField


class EditorJSONFieldTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.data = self.create_data_from_text('Hello world!')
        self.value = self.get_data_content(self.data)
        self.field = EditorJSONField()

    def testContentHTMLEqual(self):
        field_value = self.field.clean(self.value, None)
        self.assertContentHTMLEqual(field_value, '<p>Hello world!</p>')

    def testContentHTMLNotEqual(self):
        field_value = self.field.clean(self.value, None)
        self.assertContentHTMLNotEqual(field_value, '<p>Hello world</p>')

    def testFormField(self):
        self.assertIsInstance(self.field.formfield(), EditorField)
