from behave import before_all
from app.models import db, Product

@before_all
def load_data(context):
    db.create_all()
    products = [
        Product(name="Laptop", category="Electronics", price=999.99, availability=True),
        Product(name="Shirt", category="Clothing", price=29.99, availability=False)
    ]
    db.session.add_all(products)
    db.session.commit()
