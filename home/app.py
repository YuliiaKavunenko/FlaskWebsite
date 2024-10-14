import flask

home_app = flask.Blueprint(
    name = "home",
    import_name = "home",
    template_folder = "templates"
)