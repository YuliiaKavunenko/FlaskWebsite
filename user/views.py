import flask, flask_login
from main.models import User
from main.settings import db

def render_user():
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.name

        if flask.request.method == "POST":
            if flask.request.form.get("logout"):
                    print("OK LOGOU111111T")
                    flask_login.logout_user()
                    return flask.redirect("/user")
    else:
        username = "none"
    return flask.render_template(
        template_name_or_list = "user.html",
        username = username
    )
def render_registration():
    global registered
    registered = None
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.name
        if flask.request.method == "POST":
            if flask.request.form.get("logout"):
                    print("OK LOGOU111111T")
                    flask_login.logout_user()
                    return flask.redirect("/user")
    else:
        username = "none"
    if flask.request.method == "POST":
        registration = flask.request.form.get("reg-username")
        if registration != None:
            print("Hello")
            user = User(
                name = flask.request.form["reg-username"],
                password = flask.request.form["reg-password"]
            )
            print(user)
            try:
                print("add to db")
                db.session.add(user)
                db.session.commit()
                registered = True
                # data_checked = False  
                return flask.redirect(flask.url_for('user.authorization'))
            except:
                registered = False
                return "Error"
        else:
            registered = False
    return flask.render_template(
        template_name_or_list = "registration.html",
        registered = registered,
        username = username
    )

def render_authorization():
    global error_auth
    error_auth = None
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.name
        if flask.request.method == "POST":
            if flask.request.form.get("logout"):
                    print("OK LOGOU111111T")
                    flask_login.logout_user()
                    return flask.redirect("/user")
    else:
        username = "none"
    
    if flask.request.method == "POST":
        authorization = flask.request.form.get("auth-username")
        if authorization is not None:
            users = User.query.filter_by(
                name=flask.request.form["auth-username"],
                password=flask.request.form["auth-password"]
            ).all()

            if len(users) == 0:
                error_auth = True
            else:
                error_auth = False
                flask_login.login_user(users[0])
                username = users[0].name

        else:
            error_auth = None

    return flask.render_template(
        template_name_or_list="authorization.html",
        error_auth=error_auth,
        username=username
    )

#help pls, kristina rab( yulia dura
