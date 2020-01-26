from flask import Flask
#from flaskext.markdown import Markdown

def create_app(**config_overrides):
    app = Flask(__name__)

    app.config.from_pyfile("settings.py")
    app.config.update(config_overrides)

    from client_app.view import client_app

    #Markdown(app)
    
    app.register_blueprint(client_app)

    return app

