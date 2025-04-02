def test_read_product():
    product = Product(name="Laptop", category="Electronics", price=999.99, availability=True)
    db.session.add(product)
    db.session.commit()
    fetched_product = Product.query.get(product.id)
    assert fetched_product.name == "Laptop"

def test_update_product():
    product = Product(name="Phone", category="Electronics", price=499.99, availability=True)
    db.session.add(product)
    db.session.commit()
    product.price = 599.99
    db.session.commit()
    updated_product = Product.query.get(product.id)
    assert updated_product.price == 599.99
