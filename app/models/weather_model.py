from datetime import datetime


def criar_registro_clima(coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod):
    return {
        "coord": coord,
        "weather": weather,
        "base": base,
        "main": main,
        "visibility": visibility,
        "wind": wind,
        "clouds": clouds,
        "dt": dt,
        "sys": sys,
        "timezone": timezone,
        "id": id,
        "name": name,
        "cod": cod,
        "data_consulta": datetime.utcnow()
    }


def criar_consulta_clima(nome_usuario, email_usuario, consultas):
    return {
        "nome_usuario": nome_usuario,
        "email_usuario": email_usuario,
        "consultas": consultas
    }
