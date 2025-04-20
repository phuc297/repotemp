from django import template

register = template.Library()


def add_class(value, arg):
    return value.as_widget(attrs={"class": arg})


register.filter("check_following", add_class)
