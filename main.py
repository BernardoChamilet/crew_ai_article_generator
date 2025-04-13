from flask import Flask
from src.config.config import secret_key, debug, port
from src.routes.crewai_routes import crewai_bp

api = Flask(__name__)

api.config['DEBUG'] = debug
api.secret_key = secret_key

api.register_blueprint(crewai_bp)

if __name__ == '__main__':
    api.run(port=port)