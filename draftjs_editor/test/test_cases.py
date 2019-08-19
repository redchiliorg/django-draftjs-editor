import json

from django.test import SimpleTestCase
from draftjs_exporter.html import HTML


class TestCase(SimpleTestCase):
    _create_data_from_text_template = """{{
        "entityMap": {{}},
        "blocks": [{{
            "key": "6mgfh",
            "text": "{}",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": []
        }}]
    }}"""

    def create_data_from_text(self, text):
        return self._create_data_from_text_template.format(text)

    def get_data_content(self, data):
        return json.loads(data)

    def get_content_html(self, content):
        return HTML().render(content)

    def assertContentHTMLEqual(self, content, html):
        self.assertHTMLEqual(self.get_content_html(content), html)

    def assertContentHTMLNotEqual(self, content, html):
        self.assertHTMLNotEqual(self.get_content_html(content), html)
