from .abstract_model import AbstractModel
from .db import db


class StudentModel(AbstractModel):
    _collection = db["students"]

    def __init__(self, json_data):
        super().__init__(json_data)

    def _get_all(self, query: dict = {}):
        students = self.find(query)
        return [str(student) for student in students]

    def _stringfy_id(self):
        self.data["_id"] = str(self.data["_id"])
        return str(self.data)
