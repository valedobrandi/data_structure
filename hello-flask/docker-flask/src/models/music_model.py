from .abstract_model import AbstractModel
from .db import db
from dataclasses import dataclass


@dataclass
class MusicModel(AbstractModel):
    _collection = db["musics"]

    def __init__(self, json_data):
        super().__init__(json_data)