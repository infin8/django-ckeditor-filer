import fields, views, urls, models, widgets

try:
    from django.template.loader import add_to_builtins
except:
    from django.template.base import add_to_builtins

add_to_builtins('ckeditor_filer.templatetags.ckeditor_tags')
