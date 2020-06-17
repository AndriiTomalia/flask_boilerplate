from flask import Flask
from flask_cors import CORS

from src import config
from src.model import db

server = Flask(__name__)

server.debug = config.DEBUG
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI

db.init_app(server)
db.app = server

CORS(
    server,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)

from src.route.common import common_blueprint
server.register_blueprint(common_blueprint)

from src.route.user import user_blueprint
server.register_blueprint(user_blueprint)


if __name__ == '__main__':
    server.run(debug=True)
