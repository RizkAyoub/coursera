import factory
from app.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = factory.Faker('random_element', elements=('Electronics', 'Clothing', 'Books'))
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    availability = factory.Faker('boolean')
