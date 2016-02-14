from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

# Migrations
migrate = Migrate(app, db)

from users import views
from formularios import views