import os

import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

## https://flask-marshmallow.readthedocs.io/en/latest/ - https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
## https://flask-sqlalchemy.palletsprojects.com/en/2.x/

# Init app
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connexion_app = connexion.FlaskApp(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connexion_app.app

# Build the Sqlite ULR for SqlAlchemy
# sqlite_url = "sqlite:////" + os.path.join(basedir, "people.db")
sqlite_url = "sqlite:///C:\\Users\\ivlopez\\PycharmProjects\\api-flask-sqlalchemy\\people.db"

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
