import os
from flask import Flask, render_template
from namesAPI import names_api
from usersAPI import users_api
from favoritesAPI import favorites_api
from sqlalchemy_db_instance import db

project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.secret_key = os.environ["SECRET_KEY"]
    if os.environ["RUN_ENVIRONMENT"] == 'network':
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=os.environ["DB_USER"],pw=os.environ["DB_PASS"],url=os.environ["DB_URL"],db=os.environ["DB_NAME"])
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "capstone-names.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(names_api)
    app.register_blueprint(users_api)
    app.register_blueprint(favorites_api)

    return app
