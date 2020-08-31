"""This is where the routes are defined. It may be split into a package of its own"""
from flask import render_template, request
from app import app
from app.models import *


@app.route('/', methods=['GET', 'POST'])
def main_frame():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        raise NotImplementedError()
        posts = None  # get from models.py

    return render_template('...', posts=posts)  # TODO


# Error handling
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
