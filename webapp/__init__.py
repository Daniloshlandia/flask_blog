import logging
from flask import Flask, has_request_context, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_celery import Celery
from flask_caching import Cache
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_assets import Environment, Bundle
from flask_babel import Babel, _
#creating own extension youtube temporal debugging
from flask import Blueprint, render_template, Markup


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger(__name__)

db = SQLAlchemy()
migrate = Migrate()
celery = Celery()
debug_toolbar = DebugToolbarExtension()
cache = Cache()
assets_env = Environment()
mail = Mail()

main_css = Bundle(
    'css/bootstrap.css',
    filters='cssmin',
    output='css/common.css'
)

main_js = Bundle(
    'js/jquery.js',
    'js/bootstrap.js',
    filters='jsmin',
    output='js/common.js'
)


"""
Creating object Youtube function handled parameter of jinja engiene and Render
HTML to display template.
"""
class Youtube(object):
    def __init__(self, app=None, **kwargs):
        if app:
            self.init__app(app)

    def init_app(self, app):
        self.register_blueprint(app)
        app.add_template_global(youtube)

    def register_blueprint(self, app):
        module = Blueprint(
            "youtube",
            __name__,
            url_prefix='youtube',
            template_folder="templates"
        )
        app.register_blueprint(module)
        return module

class Video(object):
    def __init__(self, video_id, cls="youtube"):
        self.video_id = video_id
        self.cls = cls

        @property
        def html(self):
            return Markup(render_template('youtube/video.html', video=self))

    def youtube(*args, **kwargs):
        video = Video(*args, **kwargs)
        return video.html


youtube = Youtube()
"""
end code from own extension debugging
"""
def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)
    celery.init_app(app)
    debug_toolbar.init_app(app)
    cache.init_app(app)
    assets_env.init_app(app)
    mail.init_app(app)
#core function youtube
    youtube.init_app(app)
#core function youtube
    from .auth import create_module as auth_create_module
    from .blog import create_module as blog_create_module
    from .main import create_module as main_create_module
    from .api import create_module as api_create_module
    from .admin import create_module as admin_create_module
    from .babel import create_module as babel_create_module
    auth_create_module(app)
    blog_create_module(app)
    main_create_module(app)
    api_create_module(app)
    admin_create_module(app)
    babel_create_module(app)

    return app
