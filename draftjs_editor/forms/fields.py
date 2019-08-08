from django.contrib.postgres.forms import JSONField

from .widgets import Editor


class EditorField(JSONField):
    """Draft.js editor form field."""

    widget = Editor


__all__ = ['EditorField']
