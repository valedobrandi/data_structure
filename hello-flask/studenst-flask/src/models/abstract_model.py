from pymongo.collection import Collection, ObjectId


class AbstractModel:
    _collection: Collection = None

    def __init__(self, data: dict) -> None:
        self.data = data

    def save(self):
        post_id = self._collection.insert_one(self.data)
        return str(post_id.inserted_id)

    def update(self, id: str):
        post_id = self._collection.update_one(
            {"_id": id},
            {"$set": self.data}
            )

        return post_id

    def delete(self):
        db_return = self._collection.delete_one({"_id": ObjectId(self.data)})
        return db_return

    @classmethod
    def find(cls, query: dict = {}):
        data = cls._collection.find(query)
        return [res for res in data]

    @classmethod
    def find_one(cls, query: str):
        data = cls._collection.find_one({"_id": ObjectId(query)})
        return data
