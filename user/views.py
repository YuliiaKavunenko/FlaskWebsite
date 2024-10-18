import flask, flask_login
from main.models import User
from main.settings import db

def render_user():
    registered = None
    error_auth = None
    data_checked = None

    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.username
        registered = True
        error_auth = False
        data_checked = False

    else:
        username = "none"
        # registered = False
        if flask.request.method == "POST":
            registration = flask.request.form.get("reg-username")
            authorization = flask.request.form.get("auth-username")
            print("POST zapros")
            print(registration)
            print(authorization)
            if registration != None:
                print("Hello")
                user = User(
                    username=flask.request.form["reg-username"],
                    password=flask.request.form["reg-password"]
                )
                print(user)
                try:
                    print("add to db")
                    db.session.add(user)
                    db.session.commit()
                    registered = True
                except:
                    registered = False
                    return "Error"
                
            if authorization != None:
                data_checked = True
                users = User.query.filter_by(
                    username = flask.request.form["auth-username"],
                    password = flask.request.form["auth-password"]
                ).all()

                if len(users) == 0:
                    registered = False
                    error_auth = True
                    username = "none"
                    print("Error Authorization")
                    
                else:
                    registered = True
                    error_auth = False
                    flask_login.login_user(users[0])
                    username = users[0].username
            else:
                username = username,
                registered = False,
                error_auth = None,
                data_checked = False

                   
    return flask.render_template(
        template_name_or_list = "user.html",
        username = username,
        registered = registered,
        error_auth = error_auth,
        data_checked = data_checked
    )

#help pls, kristina rab( yulia dura