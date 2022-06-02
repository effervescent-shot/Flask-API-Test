from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
config = {
    'SQLALCHEMY_DATABASE_URI' :'sqlite:///' + os.path.join(basedir, 'db.sqlite'),
    'SQLALCHEMY_TRACK_MODIFICATION': False
}

db = SQLAlchemy()

def create_app(config=config):
    # init app
    app = Flask(__name__)
    app.config.update(config)
    register_views(app)
    register_db(app)
    
    return app

def register_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_views(app):
    # That's the simplest but retarded way of registering the views (routes)
    # More elegant way is to use Blueprints  
    with app.app_context():
        from . import views
    