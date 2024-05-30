#!/usr/bin/env python3
'''Flask Application'''
from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext
import config
app = Flask(__name__)
app.config_class(config)

babel = Babel(app, default_locale='en', default_timezone='UTC')


@babel.localeselector
def get_locale():
    '''Get locale language'''
    locale = request.args.get('locale')
    langs = config.Config.LANGUAGES
    if locale is None or locale not in langs:
        return request.accept_languages.best_match(langs)
    if locale in langs:
        return locale


@app.route('/')
def index() -> str:
    '''Index route'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=8003)
