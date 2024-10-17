import flask, flask_login
from main.models import User
from main.settings import db

def render_user():
    global error_rect, error_auth, is_authenticated, good_registration
    error_rect = False
    error_auth = False
    good_registration = None
    show_registration = True

    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.name
        is_authenticated = True
    else:
        username = "none"
        if flask.request.method == "POST":
            if flask.request.form.get("registration-form"):
                user = User(
                    username=flask.request.form["username"],
                    password=flask.request.form["password"]
                )
                try:
                    db.session.add(user)
                    db.session.commit()
                    error_rect = False
                    good_registration = True
                    show_registration = False
                except:
                    error_rect = True
            elif flask.request.form.get("authorization-form"):
                users = User.query.filter_by(
                    username = flask.request.form["username"],
                    password = flask.request.form["password"]
                ).all()
                if len(users) == 0:
                    error_auth = True
                else:
                    error_auth = False
                    flask_login.login_user(users[0])
                    username = users[0].username
                    show_registration = False

    return flask.render_template(
        template_name_or_list = "user.html",
        username = username,
        error_rect =error_rect,
        error_auth = error_auth,
        good_registration = good_registration,
        show_registration = show_registration
    )

#help pls, kristina rab( yulia dura