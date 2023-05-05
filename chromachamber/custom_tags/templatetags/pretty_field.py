from django import forms, template
from django.forms import BoundField 
from django.template.loader import get_template
from django.templatetags.static import static
from django.utils.safestring import mark_safe, SafeString
from django_simple_bulma.utils import get_js_files, logger, themes 


register = template.Library()



@register.simple_tag 
def style_sheet(theme: str="") -> SafeString:
    if theme is not None and theme not in themes:
        logger.warning("Theme not found")
        theme = ""

    css = static(f'css/{theme + "_" if theme else ""}bulma.css')
    stylesheet_id = f'bulma-css-{theme}' if theme else 'bulma-css'

    html = [
        f'<link rel="preload" href="{css}" as="style">',
        f'<link rel="stylesheet" href="{css}" id="{stylesheet_id}">'
    ]

    for js_file in map(static, get_js_files()):
        html.append(f'<script defer type="text/javascript" src="{js_file}"></script>')
    
    return mark_safe("\n".join(html))