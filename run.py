from dotenv import load_dotenv
from flask import Flask
from flask_restplus import Api

from app.gatways.database.mongodb.conn import get_db

from app.views.weather_view import api_ns

load_dotenv()

app = Flask(__name__)
api = Api(app)

get_db(app)

api.add_namespace(api_ns, path='/weather')

if __name__ == '__main__':
    app.run(debug=True)
