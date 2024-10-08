from .abstract_model import AbstractModel
from .db import db
import random


class JokeModel(AbstractModel):
    _collection = db["jokes"]

    def __init__(self, json_data):
        super().__init__(json_data)

    @classmethod
    def get_random(cls):
        data = cls.find()
        if not data:
            return
        return random.choice(data)

    def to_ditc(self):
        return {
            "_id": str(self.data["_id"]),
            "joke": self.data["joke"],
        }