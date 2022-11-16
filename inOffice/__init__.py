from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

scheduler = APScheduler()
db = SQLAlchemy()

class Config:

    SCHEDULER_JOBSTORES = {
        "default": SQLAlchemyJobStore(url="sqlite:///flask_context.db")
    }

    SCHEDULER_API_ENABLED = True

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["SECRET_KEY"] = "bigsecret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    scheduler.init_app(app)

    from .auth import auth
    from .views import views
    
    with app.app_context():
        db.create_all()
        
        @app.before_first_request
        def load_tasks():
            from . import tasks

        scheduler.start()

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app