from fastapi import FastAPI
from .product_model import ProductLibrary, StoragedProduct, Product


app = FastAPI(title="Hello World!")


@app.get("/", response_model=dict)
def home():
    return {"message": "Hello World"}


@app.get("/products/", response_model=list[StoragedProduct])
def products_list():
    return ProductLibrary.find_all()


@app.get("/products/{id_product}", response_model=StoragedProduct)
def product_by_id(id_product):
    return ProductLibrary.find_by_id(id_product)


@app.post("/products/", response_model=dict)
def add_product(product: Product):
    ProductLibrary.create(product)
    return {"message": "Product added successfully!"}


@app.delete("/products/{id_product}", response_model=dict)
def delete_product(id_product):
    ProductLibrary.delete(id_product)
    return {"message": "Product deleted successfully!"}


@app.put("/products/{id_product}", status_code=201, response_model=dict)
def update_product(id_product: str, product: Product):
    try:
        ProductLibrary.update(id_product, product)
        return {"message": "Product updated successfully!"}
    except ValueError:
        return {"message": "Product updated fail!"}, 400