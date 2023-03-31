import unittest
from src.drink import Drink
from src.bar import Bar
from src.guest import Guest
from src.song import Song

class TestBar(unittest.TestCase):

    def setUp(self):
       self.drink_pint = Drink("Pint", 4.5, 2)
       self.drink_whisky = Drink("Whisky", 7, 3)
       self.drink_cocktail = Drink("Cocktail", 10, 5)

       self.bar = Bar("Codeclan Caraoke", 3, 0, 200.00)

    def test_bar_has_name(self):
        self.assertEqual("Codeclan Caraoke", self.bar.name)

    def test_bar_has_rooms(self):
        self.assertEqual(3, self.bar.rooms)

    def test_bar_has_guests(self):
        self.assertEqual(0, self.bar.guests)
        
    def test_bar_has_till(self):
        self.assertEqual(200.00, self.bar.till)