import flask
from main.settings import mail
from flask_mail import Message

def render_home():
    user_review = flask.request.form.get("user-review")
    if flask.request.method == "POST":
        if user_review:
            name = flask.request.form.get("name")
            print(name)
            email = flask.request.form.get("email")
            print(email)
            review = flask.request.form.get("review")
            print(review)
            try:
                msg = Message(
                    subject = "новий відгук",
                    recipients = "crazycel.hihi@gmail.com",
                    body = f"клієнт {name} залишив/ла відгук:\n{review}\nпошта для зворотнього зв'язку {email}",
                    sender = "kavunenko0911@gmail.com"
                )
                mail.send(msg)
            except Exception as e:
                print(f"Помилка: {e}")
    return flask.render_template(template_name_or_list = "home.html")