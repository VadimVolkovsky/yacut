import os
import re

# MAIN_URL = 'http://localhost/'
MAIN_URL = 'http://127.0.0.1:5000/'
CUSTOM_ID_MIN_LENGTH = 1
CUSTOM_ID_MAX_LENGTH = 16
CUSTOM_ID_REGEX = fr"[a-zA-Z0-9]{{{CUSTOM_ID_MIN_LENGTH},{CUSTOM_ID_MAX_LENGTH}}}$"
CUSTOM_ID_PATTERN = re.compile(CUSTOM_ID_REGEX)
CUSTOM_ID_MAX_GENERATED_LENGTH = 6
URL = 'url'
CUSTOM_ID = 'custom_id'
ORIGINAL = 'original'
SHORT = 'short'
SHORT_LINK = 'short_link'
TEMPLATES_STATIC_DIR = 'html'
MAIN_PAGE_TEMPLATE = 'index.html'
TEMPLATE_404 = '404.html'
TEMPLATE_505 = '505.html'
INDEX_URL = '/'
REDIRECT_URL = '/<path:custom_id>'
API_GET_URL = '/api/id/<string:short_id>/'
API_ADD_URL = '/api/id/'


class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
