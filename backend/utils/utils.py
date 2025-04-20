
import os
import random


def short_text(text, word_limit=15):
    words = text.split()
    shortened = " ".join(words[:word_limit])
    return shortened


def get_random_thumbnail_1():
    folder_path = '.\mediafiles\defaultthumnail'
    files = [f for f in os.listdir(folder_path) if os.path.isfile(
        os.path.join(folder_path, f))]
    if not files:
        return None
    random_file = random.choice(files)
    random_file_path = os.path.join(folder_path, random_file)
    return random_file, random_file_path


def get_random_thumbnail():
    folder_path = '.\mediafiles\defaultthumnail'
    files = [f for f in os.listdir(folder_path) if os.path.isfile(
        os.path.join(folder_path, f))]
    if not files:
        return None
    random_file = random.choice(files)
    random_file_path = f'/defaultthumnail/{random_file}'
    return random_file_path
