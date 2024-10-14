import flask, os, flask_sqlalchemy, flask_migrate, flask_mail
from flask_mail import Mail

project = flask.Flask(
    import_name = "main",
    template_folder = "templates",
    instance_path = os.path.abspath(__file__ + "../../instance/data.db")
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app = project)
migrate = flask_migrate.Migrate(app = project, db = db)

project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["MAIL_PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_USE_SSL"] = False
project.config["MAIL_USERNAME"] = "kavunenko0911@gmail.com"
project.config["MAIL_PASSWORD"] = "kbkg zrxf crkv uqcv"

mail = Mail(project)