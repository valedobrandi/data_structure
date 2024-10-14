import random


class Book:
    def __init__(self, book: dict):
        self._id = random.randint(1, 1000)
        self._title = book["title"]
        self._author = book["author"]
        self._year = book["year"]

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    def get_book(self):
        return {
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "year": self._year,
        }
