# Import flask and template operators
from flask import Flask, render_template
from flask.ext.login import LoginManager

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Define the login manager and initialise it
login_manager = LoginManager()
login_manager.init_app(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (myapp)
from app.myapp.controllers import myapp

# Register blueprint(s)
app.register_blueprint(myapp, url_prefix='/myapp')

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()