import flask, os, flask_sqlalchemy, flask_migrate

project = flask.Flask(
    import_name = "main",
    template_folder = "templates",
    instance_path = os.path.abspath(__file__ + "../../instance/data.db")
)

project.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app = project)
migrate = flask_migrate.Migrate(app = project, db = db)