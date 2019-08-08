from django.contrib.postgres.fields import JSONField
from django.db.models.fields import TextField

from .forms import EditorField


class EditorFieldMixin:
    """Draft.js editor model field mixin."""

    def formfield(self, form_class=EditorField, **kwargs):
        """Use EditorField as default form field."""
        base = super()
        if hasattr(base, 'formfield'):
            return base.formfield(form_class=form_class, **kwargs)
        return form_class(**kwargs)


class EditorTextField(EditorFieldMixin, TextField):
    """Draft.js editor text field."""


class EditorJSONField(EditorFieldMixin, JSONField):
    """Draft.js editor postgres JSON field."""


__all__ = ['EditorTextField', 'EditorJSONField']
