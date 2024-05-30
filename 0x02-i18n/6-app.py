#!/usr/bin/env python3
'''Flask Application'''
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from pytz import all_timezones
import config
app = Flask(__name__)
app.config_class(config)

babel = Babel(app, default_locale='en', default_timezone='UTC')

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """Before any request"""
    is_user = request.args.get('login_as')
    if is_user:
        g.user = get_user(int(is_user))


@babel.localeselector
def get_locale() -> str:
    '''Get locale language'''
    locale = request.args.get('locale')
    langs = config.Config.LANGUAGES
    if locale is None or locale not in langs:
        return request.accept_languages.best_match(langs)
    if locale in langs:
        return locale


def get_user(login_as) -> Union[dict, None]:
    """Returns a user dictionary or None if the ID cannot be
     found or if login_as was not passed."""
    return users.get(login_as)


@app.route('/')
def index() -> str:
    '''Index route'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=8003)
