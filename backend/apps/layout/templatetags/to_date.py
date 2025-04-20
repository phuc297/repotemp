import datetime
from django import template

register = template.Library()


def to_date(datetime_object):
    formatted_date = datetime_object.strftime("%d/%m/%Y")
    return formatted_date


register.filter("to_date", to_date)
