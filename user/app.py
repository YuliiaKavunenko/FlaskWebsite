import flask

user_app = flask.Blueprint(
    name = "user",
    import_name = "user",
    template_folder = "templates",
    static_folder = "../static/user",
    static_url_path = "/static/user"
)
