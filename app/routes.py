# -*- coding: utf-8 -*-
from flask import jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'hello': 'Hello, this is my homework Flask!'})