from django import template

register = template.Library()


def head(set):
    return set[:5]

def head3(set):
    return set[:3]


register.filter("head", head)
register.filter("head3", head3)
