import flask, flask_login

def render_tour():
    global username
    username = "none"
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.username
    return flask.render_template(template_name_or_list= "tour.html", username = username)