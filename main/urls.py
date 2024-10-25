from home import render_home, home_app
from user import render_user, user_app
from tour import render_tour, tour_app
from .settings import project

home_app.add_url_rule(rule = "/", view_func = render_home, methods = ["GET", "POST"])
user_app.add_url_rule(rule = "/user", view_func = render_user, methods = ["GET", "POST"])
tour_app.add_url_rule(rule = "/tour", view_func = render_tour, methods = ["GET", "POST"])

project.register_blueprint(blueprint= home_app)
project.register_blueprint(blueprint = user_app)
project.register_blueprint(blueprint = tour_app)