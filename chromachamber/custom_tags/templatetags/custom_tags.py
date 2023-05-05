from django import forms, template
from django.forms import BoundField
from django.utils.html import format_html 
from django.utils.safestring import mark_safe 
from django.db.models import Count 


register = template.Library()


@register.filter(
    name="clsmarkup"
)
def cls_markup(element, class_attr):
    existing = element.field.widget.attrs.get('class') or ''
    markup = f'{existing} {class_attr}'
    return element.as_widget(
        attrs={'class': markup}
    )


@register.filter(
    name='idmarkup'
)
def id_markup(element, id_attr):
    return element.as_widget(
        attrs={'id': id_attr}
    )


@register.filter(
    name="istextarea"
)
def is_textarea(element):
    return isinstance(element, forms.Textarea)


@register.filter(
    name="getlabel"
)
def get_label(field, css_attrs=""):
    # label_tag = f'<label for="{field.label.id_for_label or ""}" class="{css_attrs}">{{ field.label }}</label>'
    # return format_html(label_tag)
    #label_for = field.
    return field.label_tag(
        attrs={
            'class': css_attrs
        }
    )
    
