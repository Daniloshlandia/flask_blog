from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_celery import Celery
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
celery = Celery()
debug_toolbar = DebugToolbarExtension()
cache = Cache()

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    migrate.init_app(app, db)
    celery.init_app(app)
    debug_toolbar.init_app(app)
    cache.init_app(app)
    
    from .auth import create_module as auth_create_module
    from .blog import create_module as blog_create_module
    from .main import create_module as main_create_module
    from .api import create_module as api_create_module
    auth_create_module(app)
    blog_create_module(app)
    main_create_module(app)
    api_create_module(app)

    return app
