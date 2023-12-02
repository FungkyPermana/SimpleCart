import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

# post new cart
def test_post_cart(client):
    cart_payload = {
        "coupon_code": "DISCOUNT123",
        "shipping_fee": 5.99,
        "cart_items": [
            {"product_id": 1, "qty": 2, "item_price": 19.99},
            {"product_id": 2, "qty": 1, "item_price": 29.99}
        ]
    }
    response = client.post("/api/cart", json=cart_payload)
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'data created'

