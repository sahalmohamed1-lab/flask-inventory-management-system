import pytest
from unittest.mock import patch
from app import app, inventory

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    inventory.clear() 

def test_get_empty_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert response.json == []

def test_add_manual_item(client):
    payload = {"product_name": "Test Milk", "price": 2.99, "stock": 10}
    response = client.post('/inventory', json=payload)
    assert response.status_code == 201
    assert response.json['product_name'] == "Test Milk"

@patch('app.requests.get')
def test_add_item_with_external_api(mock_get, client):
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {"product_name": "Mocked Almond Milk", "brands": "Silk"}
    }
    payload = {"barcode": "123456", "price": 4.99, "stock": 5}
    response = client.post('/inventory', json=payload)
    assert response.status_code == 201
    assert response.json['product_name'] == "Mocked Almond Milk"
    assert response.json['brands'] == "Silk"

def test_patch_item(client):
    client.post('/inventory', json={"product_name": "Bread", "price": 1.99, "stock": 20})
    item_id = inventory[0]['id']
    response = client.patch(f'/inventory/{item_id}', json={"stock": 15})
    assert response.status_code == 200
    assert inventory[0]['stock'] == 15

def test_delete_item(client):
    client.post('/inventory', json={"product_name": "Bread", "price": 1.99, "stock": 20})
    item_id = inventory[0]['id']
    response = client.delete(f'/inventory/{item_id}')
    assert response.status_code == 200
    assert len(inventory) == 0