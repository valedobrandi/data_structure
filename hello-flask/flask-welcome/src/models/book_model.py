from .db import db


class BooksModel:
    _collection = db["jokes"]

    def __init__(self, data):
        self.data = data

    @classmethod
    def edit(cls, json_data={}):
        print(json_data)
        edit_database = cls._collection.update_one(
            {"id": json_data["id"]},
            {
                "$set": {
                    "title": json_data["title"],
                    "author": json_data["author"],
                    "year": json_data["year"],
                }
            },
        )
        print(f"Matched count: {edit_database.matched_count}")
        print(f"Modified count: {edit_database.modified_count}")
        print(f"Upserted ID: {edit_database.upserted_id}")
        return edit_database

    @classmethod
    def delete(cls, json_data={}):
        result = cls._collection.delete_many({"id": json_data["id"]})
        return result

    @classmethod
    def save(cls, json_data={}):
        result = cls._collection.insert_one(json_data)
        return result

    @classmethod
    def find(cls, query={}):
        data = cls._collection.find(query)
        return [cls(book_detail) for book_detail in data]

    @classmethod
    def find_one(cls, query={}):
        data = cls._collection.find_one(query)
        return cls(data)

    def to_dict(self):
        return {
            "id": self.data.get("id"),
            "title": self.data.get("title"),
            "author": self.data.get("author"),
            "year": self.data.get("year"),
        }
