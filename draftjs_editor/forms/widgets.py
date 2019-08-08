import json

from django.utils.safestring import mark_safe
from django.forms.widgets import Textarea


class Editor(Textarea):
    """Draft.js editor form field widget."""

    template_name = 'draftjs_editor/widgets/editor.html'
    props = {
        'blockTypes': [
            {'label': 'H1', 'style': 'header-one'},
            {'label': 'H2', 'style': 'header-two'},
            {'label': 'H3', 'style': 'header-three'},
            {'label': 'H4', 'style': 'header-four'},
            {'label': 'H5', 'style': 'header-five'},
            {'label': 'H6', 'style': 'header-six'},
            {'label': 'Blockquote', 'style': 'blockquote'},
            {'label': 'UL', 'style': 'unordered-list-item'},
            {'label': 'OL', 'style': 'ordered-list-item'},
            {'label': 'Code Block', 'style': 'code-block'},
        ],
        'inlineStyles': [
            {'label': 'Bold', 'style': 'BOLD'},
            {'label': 'Italic', 'style': 'ITALIC'},
            {'label': 'Underline', 'style': 'UNDERLINE'},
            {'label': 'Monospace', 'style': 'CODE'},
        ]
    }

    def __init__(self, attrs=None, props=None):
        """Allow optional extension of widget props in init."""
        super().__init__(attrs)
        if props:
            self.props = self.props.copy()
            self.props.update(**props)

    def get_context(self, name, value, attrs):
        """Add props to context."""
        context = super().get_context(name, value, attrs)
        context['widget']['props'] = mark_safe(json.dumps(self.props))
        return context

    class Media:
        css = {
            "all": [
                'https://unpkg.com/draft-js@0.11.0/dist/Draft.css',
                'draftjs_editor/css/editor.css'
            ]
        }
        js = [
            'https://unpkg.com/react@16.8.6/umd/react.development.js',
            'https://unpkg.com/react-dom@16.8.6/umd/react-dom.development.js',
            'https://unpkg.com/immutable@3.7.4/dist/immutable.js',
            'https://unpkg.com/draft-js@0.11.0/dist/Draft.js',
            'draftjs_editor/js/StyleButton.js',
            'draftjs_editor/js/StyleControls.js',
            'draftjs_editor/js/EditorWidget.js'
        ]


__all__ = ['Editor']
