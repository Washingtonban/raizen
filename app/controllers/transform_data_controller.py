from bson import ObjectId
from datetime import datetime


class DataTransformer:

    @staticmethod
    def transform(obj):
        if isinstance(obj, list):
            return [DataTransformer.transform(item) for item in obj]
        if isinstance(obj, dict):
            return {key: DataTransformer.transform(value) for key, value in obj.items()}
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
