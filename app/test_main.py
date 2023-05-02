from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_completed():
    response = client.post(
        "/solution/",
        json= {
            'orders': [
                {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"}, 
                {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
                ],
            'criterion': "completed"
            })
    assert response.status_code == 200
    assert response.json() == 1299.69

def test_canceled():
    response = client.post(
        "/solution/",
        json= {
            'orders': [
                {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"}, 
                {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
                ],
            'criterion': "canceled"
            })
    assert response.status_code == 200
    assert response.json() == 99.96

def test_pending():
    response = client.post(
        "/solution/",
        json= {
            'orders': [
                {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"}, 
                {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
                ],
            'criterion': "pending"
            })
    assert response.status_code == 200
    assert response.json() == 999.9

def test_all():
    response = client.post(
        "/solution/",
        json= {
            'orders': [
                {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"}, 
                {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
                ],
            'criterion': "all"
            })
    assert response.status_code == 200
    assert response.json() == 2399.55
    