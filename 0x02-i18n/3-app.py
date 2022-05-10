#!/usr/bin/env python3
"""Module: Basic Flask App"""

from flask_babel import Babel
from flask import Flask, render_template, request
from os import getenv


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class: Configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def home_page():
    """Function: Home Page 0-index.html"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Function: to determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
