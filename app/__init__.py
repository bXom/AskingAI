from flask import Flask
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config_class)

  from .routes import captcha_route, file_route
  app.register_blueprint(captcha_route, url_prefix='/captcha')
  app.register_blueprint(file_route, url_prefix='/file')

  return app