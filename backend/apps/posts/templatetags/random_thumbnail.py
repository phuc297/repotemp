from django import template
import os
import random
register = template.Library()


@register.simple_tag
def random_thumnail():
    return get_random_thumbnail()


def get_random_thumbnail():
    folder_path = './static/defaultthumnail'
    files = [f for f in os.listdir(folder_path) if os.path.isfile(
        os.path.join(folder_path, f))]
    if not files:
        return None
    random_file = random.choice(files)
    random_file_path = f'/static/defaultthumnail/{random_file}'
    return random_file_path
