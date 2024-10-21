from app.product_model import ProductLibrary
import pytest


def test_hello_worlds(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_list_products(client):
    data = {
        "name": "Produto 1",
        "price": 10.0,
        "description": "Description product 1",
        "image": "https://image.com/image1.jpg",
    }

    ProductLibrary._collection.insert_one(data)
    response = client.get("/products")

    for item in response.json():
        assert "name" in item
        assert "price" in item


def test_list_products_by_id(client):
    product_id = ProductLibrary.find_all()[0].id
    ProductLibrary._collection.find_one({})
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json() == {
        "_id": product_id,
        "name": "Produto 1",
        "price": 10.0,
        "description": "Description product 1",
        "image": "https://image.com/image1.jpg",
    }


def test_add_product(client):
    data = {
        "name": "Produto 2",
        "price": 20.0,
        "description": "Description product 2",
        "image": "https://image.com/image2.jpg",
    }

    response = client.post("/products", json=data)

    assert response.status_code == 200
    assert response.json() == {"message": "Product added successfully!"}

    name = ProductLibrary.find_all()[-1].name

    assert name == "Produto 2"


def test_delete_product(client):
    product_id = ProductLibrary.find_all()[-1].id
    response = client.delete(f"/products/{product_id}")

    assert response.status_code == 200
    assert len(ProductLibrary.find_all()) == 1
    with pytest.raises(ValueError):
        ProductLibrary.find_by_id(product_id)


def test_update_product(client):
    product_id = ProductLibrary.find_all()[0].id

    data = {
        "name": "Produto 3",
        "price": 30.0,
        "description": "Description product 3",
        "image": "https://image.com/image3.jpg",
    }

    response = client.put(f"/products/{product_id}", json=data)

    assert response.status_code == 201

    update_product = ProductLibrary.find_all()[0]
    assert update_product.name == "Produto 3"
    assert update_product.price == 30.0
    assert update_product.description == "Description product 3"
