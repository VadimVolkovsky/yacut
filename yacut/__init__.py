import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

template_dir = os.path.abspath('html')
static_dir = os.path.abspath('html')
app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir,
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
