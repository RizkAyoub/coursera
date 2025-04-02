from behave import given, when, then
from app.models import Product

@given('I have products in the database')
def step_impl(context):
    context.products = [
        Product(name="Laptop", category="Electronics", price=999.99, availability=True),
        Product(name="Shirt", category="Clothing", price=29.99, availability=False)
    ]

@when('I search for products in the "{category}" category')
def step_impl(context, category):
    context.filtered_products = [p for p in context.products if p.category == category]

@then('I should see only products in the "{category}" category')
def step_impl(context, category):
    assert all(p.category == category for p in context.filtered_products)
