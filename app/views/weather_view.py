from flask_restplus import Resource, fields, Namespace, reqparse
from flask import request

from app.controllers.weather_controller import WeatherController
from app.controllers.open_weather_map_controller import OpenWeatherMapController

api_ns = Namespace('weather', description='Weather operations')

post_weather_model = api_ns.model('WeatherModel', {
    'nome': fields.String(required=True, description='Nome do usuário que consulta'),
    'email': fields.String(required=True, description='Email do usuário que consulta')
})

parser = reqparse.RequestParser()
parser.add_argument('nome', required=False, help="Nome do usuário")
parser.add_argument('email', required=False, help="E-mail do usuário")


@api_ns.route('/')
class WeatherView(Resource):

    @api_ns.expect(parser)
    def get(self):
        args = parser.parse_args()

        nome = args.get('nome')
        email = args.get('email')
        wc = WeatherController()

        if nome:
            consulta = wc.read(nome)
            return consulta, 200

        users = wc.read_all()
        consulta = {"consulta": users}
        return consulta, 200


@api_ns.route('/<string:cidade>')
class WeatherCityView(Resource):

    @api_ns.expect(post_weather_model)
    def post(self, cidade):
        data = request.json

        nome = data.get('nome')
        email = data.get('email')

        owmc = OpenWeatherMapController()
        weather = owmc.read(cidade)

        wc = WeatherController()
        consulta = wc.create(nome, email, weather)
        return consulta, 200

    @api_ns.expect(parser)
    def get(self, cidade):
        args = parser.parse_args()

        nome = args.get('nome')
        email = args.get('email')

        wc = WeatherController()

        owmc = OpenWeatherMapController()
        weather = owmc.read(cidade)

        consulta = wc.create(nome, email, weather)
        return consulta, 200
