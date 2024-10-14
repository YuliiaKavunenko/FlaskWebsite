import flask

tour_app = flask.Blueprint(
name= "tour",
import_name= "tour",
static_folder= "static/tour",
template_folder= "templates"
)