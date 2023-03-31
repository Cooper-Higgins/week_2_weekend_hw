import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
       self.drink_pint = Drink("Pint", 4.5, 2)
       self.drink_whisky = Drink("Whisky", 7, 3)
       self.drink_cocktail = Drink("Cocktail", 10, 5)

    def test_drink_has_name(self):
        self.assertEqual("Pint", self.drink_pint.name)

    def test_drink_has_price(self):
        self.assertEqual(7, self.drink_whisky.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(5, self.drink_cocktail.alcohol_level)

