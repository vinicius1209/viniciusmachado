from flask import Flask

# Flask Definitions
app = Flask(__name__)

from . import views

def execute_app():
    return app