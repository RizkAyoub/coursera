def test_list_all_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_find_by_category(client):
    response = client.get('/products?category=Electronics')
    assert response.status_code == 200
    assert all(product['category'] == 'Electronics' for product in response.json)
