from django import forms, template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Count


register = template.Library()


@register.filter(
    name="readable"
)
def make_readable(text):
    paragraphs = text.split('\n')
    paragraphs = [p for p in paragraphs if len(p) > 0]
    paragraphs = [p.replace('\t', '<p>') for p in paragraphs]
    output = '</p>'.join(paragraphs)
    return format_html(output)


@register.filter(
    name="label"
)
def style_label(field, css_class):
    label = field.label
    id_for_label = field.id_for_label or ""
    return format_html(
        f'<label for="{id_for_label}" class="{css_class}">'
    )


@register.filter(
    name='field'
)
def style_field(field, css_class):
    classes = field.field.widget.attrs.get('class', '')
    return field.as_widget(
        attrs={'class': f'{classes} {css_class}'}
    )


@register.filter(
    name='istextarea'
)
def is_textarea(field):
    return isinstance(field, forms.Textarea)


 