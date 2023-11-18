from bson import ObjectId
from datetime import datetime

from app.controllers.transform_data_controller import DataTransformer


def test_transform_objectid_to_str():
    obj_id = ObjectId()
    transformed = DataTransformer.transform(obj_id)
    assert isinstance(transformed, str)


def test_transform_datetime_to_isoformat():
    dt = datetime.now()
    transformed = DataTransformer.transform(dt)
    assert isinstance(transformed, str)
    assert transformed == dt.isoformat()


def test_transform_dict():
    obj_id = ObjectId()
    dt = datetime.now()
    test_dict = {"id": obj_id, "date": dt, "name": "Test"}
    transformed = DataTransformer.transform(test_dict)
    assert transformed["id"] == str(obj_id)
    assert transformed["date"] == dt.isoformat()
    assert transformed["name"] == "Test"


def test_transform_list():
    obj_id = ObjectId()
    dt = datetime.now()
    test_list = [obj_id, dt, "Test"]
    transformed = DataTransformer.transform(test_list)
    assert transformed[0] == str(obj_id)
    assert transformed[1] == dt.isoformat()
    assert transformed[2] == "Test"


def test_transform_nested_dict():
    obj_id = ObjectId()
    dt = datetime.now()
    test_dict = {"level1": {"id": obj_id, "date": dt}}
    transformed = DataTransformer.transform(test_dict)
    assert transformed["level1"]["id"] == str(obj_id)
    assert transformed["level1"]["date"] == dt.isoformat()


def test_transform_list_of_lists():
    obj_id = ObjectId()
    dt = datetime.now()
    test_list = [[obj_id, dt], ["Test"]]
    transformed = DataTransformer.transform(test_list)
    assert transformed[0][0] == str(obj_id)
    assert transformed[0][1] == dt.isoformat()
    assert transformed[1][0] == "Test"


def test_transform_empty_dict():
    test_dict = {}
    transformed = DataTransformer.transform(test_dict)
    assert transformed == {}


def test_transform_empty_list():
    test_list = []
    transformed = DataTransformer.transform(test_list)
    assert transformed == []
