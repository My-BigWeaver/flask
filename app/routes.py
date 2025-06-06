from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return {'message': 'Welcome to the Flask API'}