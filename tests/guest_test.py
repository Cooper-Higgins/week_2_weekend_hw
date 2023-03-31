import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
       self.song1 = Song("Simply The Best", "Tina Turner")
       self.song2 = Song("Get Away", "Chvrches")
       self.song3 = Song("Luca's Atlas", "Blackened Heart")
       self.song4 = Song("Sam Fender", "Seventeen Going Under")
       self.guest1 = Guest("Robert", 100.00, self.song1, 35, 0)
       self.guest2 = Guest("Graeme", 100.00, self.song2, 31, 0)
       self.guest3 = Guest("Scott", 100.00, self.song3, 34, 0)
       self.guest4 = Guest("David", 100.00, self.song4, 31, 0)

    def test_guest_has_name(self):
        self.assertEqual("Robert", self.guest1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song1.title, self.guest1.fav_song.title)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest1.wallet)

    def test_guest_has_drunkennness(self):
        self.assertEqual(0, self.guest1.drunkenness)

    def test_customer_has_age(self):
        self.assertEqual(35, self.guest1.age)

    
