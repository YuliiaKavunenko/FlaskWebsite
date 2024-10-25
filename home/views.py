import flask, flask_login
from main.settings import mail
from flask_mail import Message

def render_home():
    error = None
    global username
    username = "none"
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.name
        if flask.request.method == "GET":
            flask_login.logout_user()
            print("5673894504372634758 lololol")
            flask.redirect("/user")
    if flask.request.method == "POST":
        if flask.request.form.get("name"):
            name = flask.request.form.get("name")
            print(name)
            email = flask.request.form.get("email")
            print(email)
            review = flask.request.form.get("review")
            print(review)
            try:
                msg = Message(
                    subject = "новий відгук",
                    recipients = ["crazycel.hihi@gmail.com"],
                    body = f"клієнт {name} залишив/ла відгук:\n{review}\nпошта для зворотнього зв'язку {email}",
                    sender = "kavunenko0911@gmail.com"
                )
                mail.send(msg)
                error = False
            except Exception as e:
                print(f"Помилка: {e}")
                error = True
        
    return flask.render_template(template_name_or_list = "home.html", error = error, username = username)
