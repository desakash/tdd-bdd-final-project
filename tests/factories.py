import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from faker import Faker
from service.models import Product, Category

# Initialize a Faker instance
fake = Faker()

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""
        model = Product

    id = factory.Sequence(lambda n: n)  # Unique ID for each product
    name = FuzzyChoice(
        choices=[
            "Hat",
            "Pants",
            "Shirt",
            "Apple",
            "Banana",
            "Pots",
            "Towels",
            "Ford",
            "Chevy",
            "Hammer",
            "Wrench"
        ]
    )
    description = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=250))  # Random fake text
    price = FuzzyDecimal(0.5, 2000.0, 2)  # Generates a decimal price between 0.5 and 2000.0
    available = FuzzyChoice(choices=[True, False])  # Randomly chooses True or False
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )  # Randomly chooses a category from the Category enum
