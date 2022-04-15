from django import template

register = template.Library()


@register.filter
def getfilename(value):
    return value.filename()


@register.filter
def getfilepath(value):
    return str(value.file())
