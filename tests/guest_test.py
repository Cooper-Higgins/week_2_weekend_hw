import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.drink import Drink
from src.food import Food

class TestGuest(unittest.TestCase):

    def setUp(self):
       self.song1 = Song("Simply The Best", "Tina Turner")
       self.song2 = Song("Get Away", "Chvrches")
       self.song3 = Song("Luca's Atlas", "Blackened Heart")
       self.song4 = Song("Sam Fender", "Seventeen Going Under")

       self.guest1 = Guest("Robert", 100.00, self.song1, 55, 95)
       self.guest2 = Guest("Graeme", 100.00, self.song2, 31, 0)
       self.guest3 = Guest("Scott", 2.00, self.song3, 34, 40)
       self.guest4 = Guest("David", 5.00, self.song4, 31, 0)

       self.room_1 = Room("Mr. Beast", 15, 6)
       self.room_2 = Room("The Hawk is Howling", 20, 8)
       self.room_3 = Room("Rave Tapes", 25, 10)

       self.drink_pint = Drink("Pint", 4.5, 2)
       self.drink_whisky = Drink("Whisky", 7, 3)
       self.drink_cocktail = Drink("Cocktail", 10, 5)

       self.food_chips = Food("Chips", 3.99, 3)
       self.food_wings = Food("Wings", 7.99, 5)
       self.food_burger = Food("Burger", 11.99, 8)

    def test_guest_has_name(self):
        self.assertEqual("Robert", self.guest1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song1.title, self.guest1.fav_song.title)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest1.wallet)

    def test_guest_has_drunkennness(self):
        self.assertEqual(40, self.guest3.drunkenness)

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
        self.assertEqual(100, self.guest1.drunkenness)

    def test_guest_can_buy_drink_decreases_drunkenness(self):
        self.guest1.buy_food(self.food_wings)
        self.assertEqual(90, self.guest1.drunkenness)

    def test_guest_cannot_buy_drink_if_insufficient_funds(self):
        self.guest4.buy_drink(self.drink_whisky)
        self.assertEqual(5.0, self.guest4.wallet)
        self.assertEqual(0, self.guest4.drunkenness)

    def test_guest_cannot_buy_food_if_insufficient_funds(self):
        self.guest3.buy_food(self.food_burger)
        self.assertEqual(2.0, self.guest3.wallet)
        self.assertEqual(40, self.guest3.drunkenness)
