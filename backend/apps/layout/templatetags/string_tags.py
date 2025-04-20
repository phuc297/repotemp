from django import template
import faker

register = template.Library()


@register.filter
def cut(string):
    return string[:35]


@register.filter
def shorten(text, word_limit=10):
    words = text.split()
    shortened = " ".join(words[:word_limit])
    return shortened + ("..." if len(words) > word_limit else "")


@register.simple_tag
def random_sentence():
    return faker.Faker().sentence(10, 15)
