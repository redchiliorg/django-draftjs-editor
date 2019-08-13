import json

from django.conf import settings
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe


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
                'draftjs_editor/Draft.css',
                'draftjs_editor/draftjs_editor.css'
            ]
        }
        js = [
            'draftjs_editor/react.development.js'
            if settings.DEBUG else
            'draftjs_editor/react.production.min.js',

            'draftjs_editor/react-dom.development.js'
            if settings.DEBUG else
            'draftjs_editor/react-dom.production.min.js',

            'draftjs_editor/immutable.js'
            if settings.DEBUG else
            'draftjs_editor/immutable.min.js',

            'draftjs_editor/Draft.js'
            if settings.DEBUG else
            'draftjs_editor/Draft.min.js',

            'draftjs_editor/StyleButton.js',
            'draftjs_editor/StyleControls.js',
            'draftjs_editor/EditorWidget.js'
        ]


__all__ = ['Editor']
