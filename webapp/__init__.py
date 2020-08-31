""" This module initializes the application and brings together all of the various components"""
from flask import Flask
from app import views, models

# Creat the Flask App instance and load config variables from instance folder
app = Flask(__name__, static_folder="webapp/static", template_folder="webapp/templates", instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
