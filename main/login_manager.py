import flask_login
from .settings import project
from .models import User

project.secret_key = '9898922787323'
login = flask_login.LoginManager(app =  project)

@login.user_loader
def load(id):
    return User.query.get(id)
