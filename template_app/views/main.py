from flask import Blueprint, render_template, request, make_response

main = Blueprint('main', __name__)
#this is where you import the stuff you need from the app __init__




def index():
    return render_template('index.html', title='Template Flask App')

