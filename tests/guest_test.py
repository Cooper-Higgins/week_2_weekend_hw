import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.drink import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):
       self.song1 = Song("Simply The Best", "Tina Turner")
       self.song2 = Song("Get Away", "Chvrches")
       self.song3 = Song("Luca's Atlas", "Blackened Heart")
       self.song4 = Song("Sam Fender", "Seventeen Going Under")

       self.guest1 = Guest("Robert", 100.00, self.song1, 55, 0)
       self.guest2 = Guest("Graeme", 100.00, self.song2, 31, 0)
       self.guest3 = Guest("Scott", 100.00, self.song3, 34, 0)
       self.guest4 = Guest("David", 100.00, self.song4, 31, 0)

       self.room_1 = Room("Mr. Beast", 15, 6)
       self.room_2 = Room("The Hawk is Howling", 20, 8)
       self.room_3 = Room("Rave Tapes", 25, 10)

       self.drink_pint = Drink("Pint", 4.5, 2)
       self.drink_whisky = Drink("Whisky", 7, 3)
       self.drink_cocktail = Drink("Cocktail", 10, 5)

    def test_guest_has_name(self):
        self.assertEqual("Robert", self.guest1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song1.title, self.guest1.fav_song.title)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest1.wallet)

    def test_guest_has_drunkennness(self):
        self.assertEqual(0, self.guest1.drunkenness)

    def test_customer_has_age(self):
        self.assertEqual(55, self.guest1.age)

    def test_guest_can_pay_entry_fee_reduces_wallet(self):
        self.guest1.pay_entry_fee(self.room_1)
        self.assertEqual(85.00, self.guest1.wallet)

    def test_guest_can_buy_drink_decreases_wallet(self): 
        self.guest1.buy_drink(self.drink_cocktail)
        self.assertEqual(90.00, self.guest1.wallet)

    def test_guest_can_buy_drink_increases_drunkenness(self):
        self.guest1.buy_drink(self.drink_cocktail)
        self.assertEqual(5, self.guest1.drunkenness)
    
