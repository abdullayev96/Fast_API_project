from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


#
# def test_create_product():
#     response = client.post("/products/", json={"name": "Test Product", "description": "Test", "price": 10.0, "stock": 100})
#     assert response.status_code == 200
#     assert response.json()["name"] == "Test Product"
#
#
#
# def test_create_order():
#     product_response = client.post("/products/", json={"name": "Product 1", "description": "Description", "price": 5.0, "stock": 50})
#     product_id = product_response.json()["id"]
#
#     order_response = client.post("/orders/", json={"items": [{"product_id": product_id, "quantity": 5}]})
#     assert order_response.status_code == 200
#



def test_create_product():
    response = client.post("/products", json={
        "name": "Sample Product",
        "description": "This is a test product",
        "price": 10.0,
        "stock_quantity": 100
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Sample Product"
