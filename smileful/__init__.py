import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)


config_path = os.environ.get("CONFIG_PATH", "smileful.config.DevelopmentConfig")
app.config.from_object(config_path)
db = SQLAlchemy(app)

import views
import login

from database import Base, engine
Base.metadata.create_all(engine)

