import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food_chips = Food("Chips", 3.99, 3)
        self.food_wings = Food("Wings", 7.99, 5)
        self.food_burger = Food("Burger", 11.99, 8)

    def test_food_has_name(self):
        self.assertEqual("Chips", self.food_chips.name)
        
    def test_food_has_price(self):
        self.assertEqual(7.99, self.food_wings.price)
        
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(8, self.food_burger.rejuvenation_level)