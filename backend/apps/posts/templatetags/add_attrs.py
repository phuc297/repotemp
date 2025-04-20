from django import template

register = template.Library()


@register.filter
def add_class(value, arg):
    return value.as_widget(attrs={"class": arg})


@register.filter
def add_id(value, arg):
    return value.as_widget(attrs={"id": arg})
