import os
from dotenv import load_dotenv

load_dotenv('.env.dev')

print(os.environ.get('DJANGO_ALLOWED_HOSTS'))