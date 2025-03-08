from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/hello')
def hello_with_template():
    return render_template('hello.html')

@main.route('/<username>')
def show_user_profile(username):
    return f'Hello {username} and welcome to the paralympics app'