import unittest
from src.song import Song
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room_1 = Room("Mr. Beast", 15, 6)
       self.room_2 = Room("The Hawk is Howling", 20, 8)
       self.room_3 = Room("Rave Tapes", 25, 10)

       self.song1 = Song("Simply The Best", "Tina Turner")
       self.song2 = Song("Get Away", "Chvrches")
       self.song3 = Song("Luca's Atlas", "Blackened Heart")
       self.song4 = Song("Sam Fender", "Seventeen Going Under")

       self.guest1 = Guest("Robert", 100.00, self.song1, 35, 0)
       self.guest2 = Guest("Graeme", 100.00, self.song2, 31, 0)
       self.guest3 = Guest("Scott", 100.00, self.song3, 34, 0)
       self.guest4 = Guest("David", 100.00, self.song4, 31, 0)

    def test_room_has_name(self):
        self.assertEqual("Mr. Beast", self.room_1.name)

    def test_room_has_entry_fee(self):
        self.assertEqual(15, self.room_1.entry_fee)

    def test_room_capacity(self):
        self.assertEqual(8, self.room_2.capacity)

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room_1.guests))

    def test_can_add_guest_to_room(self):
        self.room_1.check_in_guests_to_room(self.guest1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_can_check_out_guest_of_room(self):
        self.room_1.check_out_guests_of_room()
        self.assertEqual(0, len(self.room_1.guests))

    def test_can_add_song_to_room_playlist(self):
        self.room_1.add_song_to_room_playlist(self.song2)
        self.assertEqual(1, len(self.room_1.playlist))