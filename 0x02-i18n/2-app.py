#!/usr/bin/env python3
'''Flask Application'''
import typing
from flask import Flask, render_template, request
from flask_babel import Babel
import config
app = Flask(__name__)
app.config_class(config)
babel = Babel(app, default_locale='en', default_timezone='UTC')


@babel.localeselector
def get_locale() -> typing.Union[str, None]:
    '''Get locale language'''
    return request.accept_languages.best_match(config.Config.LANGUAGES)


@app.route('/')
def index() -> str:
    '''Index route'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port=8003)
