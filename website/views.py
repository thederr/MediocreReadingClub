from flask import Blueprint, render_template

## Defining that this file is a blueprint of our applicaiton ###
## We have to register these blueprints in our init.py ##
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")