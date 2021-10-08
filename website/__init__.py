from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME="databse.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'd5f4g35fd4h15gfd1vb354 fdgkjfdghfdg54!#%^&*RHBvbdfvb'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    ## Initializing Databse ##
    db.init_app(app)
    ## Blueprints ##
    from .views import views
    from .auth import auth
    ## Registering Blueprints ##
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/') ##url-prefix is a way to make nested dmatheny.ninja/nest1/nest2  vs dmatheny.ninja/auth/nest1 /nested2 ##
    ## Database Creation ##
    from .models import User, Note
    create_database(app)
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
         db.create_all(app=app)
    print(' * SQLAlchemy database is running')

