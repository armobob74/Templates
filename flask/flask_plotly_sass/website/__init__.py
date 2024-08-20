from flask import Flask
import warnings
import sass
import os
from .views import views
from .api import api

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = 'NOT_SECURE_KEY'
    warnings.warn(f"FLASK_SECRET_KEY not found in environment; defaulting to {SECRET_KEY}")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    sass.compile(dirname=('./website/static/sass', './website/static/css'))
    app.register_blueprint(views)
    app.register_blueprint(api)
    return app
