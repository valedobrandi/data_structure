from .abstract_model import AbstractModel
from .db import db


class VideoModel(AbstractModel):
    _collection = db["videos_document"]

    @classmethod
    def _buscar_filmes_por_titulo(cls, titulo):
        data = cls.find({"titulo": titulo})
        return data

    def to_dict(self):
        filme = {
            "titulo": self.data["titulo"],
            "ano": self.data["ano"],
            "diretor": self.data["diretor"],
            "genero": self.data["genero"],
            "poster": self.data["poster"],
            "_id": str(self.data["_id"]),
        }

        return filme
