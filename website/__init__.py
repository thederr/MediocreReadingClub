from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'd5f4g35fd4h15gfd1vb354 fdgkjfdghfdg54!#%^&*RHBvbdfvb'

    ## Blueprints ##
    from .views import views
    from .auth import auth
    ## Blueprints ##

    ## Registering Blueprints ##
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/') ##url-prefix is a way to make nested dmatheny.ninja/auth/nest1/nested2 ##
    ## Registering Blueprints ##


    
    return app