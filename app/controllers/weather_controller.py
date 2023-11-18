from flask import current_app as app

from app.controllers.transform_data_controller import DataTransformer
from app.models.weather_model import criar_consulta_clima, criar_registro_clima


class WeatherController:

    @staticmethod
    def create(nome_usuario, email_usuario, dados_clima):
        db = app.db
        consulta = criar_registro_clima(**dados_clima)
        usuario = db.consulta_clima.find_one({"nome_usuario": nome_usuario})

        if usuario:
            db.consulta_clima.update_one(
                {"nome_usuario": nome_usuario},
                {"$push": {"consultas": consulta}}
            )
            return DataTransformer.transform(consulta)

        consulta_clima = criar_consulta_clima(nome_usuario, email_usuario, [consulta])
        db.consulta_clima.insert_one(consulta_clima)
        return DataTransformer.transform(consulta)

    @staticmethod
    def read(nome_usuario):
        db = app.db
        usuario = db.consulta_clima.find_one({"nome_usuario": nome_usuario})
        return DataTransformer.transform(usuario)

    @staticmethod
    def read_all():
        db = app.db
        users = list(db.consulta_clima.find({}))
        return DataTransformer.transform(users)
