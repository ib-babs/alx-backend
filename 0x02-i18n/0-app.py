#!/usr/bin/env python3
'''Flask Application'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    '''Index route'''
    return render_template('0-index.html')
