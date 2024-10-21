from bson import ObjectId
from .database import db
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: float
    description: str
    image: str


class StoragedProduct(Product):
    id: str = Field(alias="_id")


class ProductLibrary:
    _collection = db["products"]

    @classmethod
    def find_all(cls):
        return [
            StoragedProduct(_id=str(product.pop("_id")), **product)
            for product in cls._collection.find()
        ]

    @classmethod
    def find_by_id(cls, product_id: str):
        found_product = cls._collection.find_one({"_id": ObjectId(product_id)})

        if found_product:
            return StoragedProduct(
                _id=str(found_product.pop("_id")),
                **found_product
            )

        raise ValueError("Product not found")

    @classmethod
    def create(cls, product: Product):
        cls._collection.insert_one(product.__dict__)

    @classmethod
    def delete(cls, product_id: str):
        cls._collection.delete_one({"_id": ObjectId(product_id)})

    @classmethod
    def update(cls, product_id: str, product: Product):
        response = cls._collection.update_one(
            {"_id": ObjectId(product_id)}, {"$set": product.__dict__}
        )

        if response.modified_count:
            return

        raise ValueError("Product not found")
