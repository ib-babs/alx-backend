#!/usr/bin/env python3
'''Flask Application'''
from flask import Flask, render_template, g, request
from flask_babel import Babel
import config
app = Flask(__name__)
app.config_class(config)
babel = Babel(app, default_locale='en', default_timezone='UTC')


@app.route('/')
def index() -> str:
    '''Index route'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=8003)
