from flask import Flask
from app.manage.views import manage


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(manage)

