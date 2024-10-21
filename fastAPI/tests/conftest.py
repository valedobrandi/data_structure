from fastapi.testclient import TestClient
from app.product_model import ProductLibrary
from app.main import app
import pytest


@pytest.fixture(autouse=True)
def client():
    return TestClient(app)


@pytest.fixture(autouse=True, scope="module")
def empty_database():
    ProductLibrary._collection.delete_many({})
