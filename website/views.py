from flask import Blueprint

## Defining that this file is a blueprint of our applicaiton ###
## We have to register these blueprints in out init.py ##
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> 3 Guys and a Hot Tub </h1>"
