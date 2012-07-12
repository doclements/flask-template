from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from template_app import settings
from template_app.core import setup_routing

# setup application
app = Flask('template_app')
app.config.from_object(settings)

import logging
from logging.handlers import RotatingFileHandler
f_handler = RotatingFileHandler('test.log')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(filename)s:%(lineno)d]'
))
app.logger.addHandler(f_handler)

import yaml 

config = yaml.load(open('/home/olly/flasktemplate/template_app/config.yaml' , 'r'))

# setup database
db = SQLAlchemy(app)



# register application views and blueprints
from template_app.urls import routes
setup_routing(app, routes)

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()
