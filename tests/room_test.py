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
       self.song4 = Song("George Ezra", "Budapest")
       self.song5 = Song("Stick Stickly", "Attack Attack!")
       self.song6 = Song("Helvegan", "Wardruna")
       self.song7 = Song("MakeThisRelate", "Pick Your Side")
       self.song8 = Song("Mogwai", "To The Bin My Friend, Tonight We Vacate Earth")

       self.guest1 = Guest("Robert", 100.00, self.song1, 55, 0)
       self.guest2 = Guest("Graeme", 100.00, self.song2, 31, 0)
       self.guest3 = Guest("Scott", 100.00, self.song3, 33, 0)
       self.guest4 = Guest("David", 100.00, self.song4, 31, 0)
       self.guest5 = Guest("Christopher", 100.00, self.song5, 31, 0)
       self.guest6 = Guest("Calum", 100.00, self.song6, 31, 0)
       self.guest7 = Guest("Danny", 100.00, self.song7, 32, 0)
       self.guest8 = Guest("Jamie", 5.00, self.song8, 31, 0)

       self.large_party = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5, self.guest6, self.guest7, self.guest8]

    def test_room_has_name(self):
        self.assertEqual("Mr. Beast", self.room_1.name)

    def test_room_has_entry_fee(self):
        self.assertEqual(15, self.room_1.price)

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

    def test_add_more_guests_than_room_capacity(self):
        expected_value = "No room at the inn"
        actual_value = self.room_1.no_room_at_the_inn(self.large_party, self.room_1.capacity)
        self.assertEqual(expected_value, actual_value)

    def test_add_less_guests_than_room_capacity(self):
        expected_value = "Come on in!"
        actual_value = self.room_3.no_room_at_the_inn(self.large_party, self.room_3.capacity)
        self.assertEqual(expected_value, actual_value)

    def test_guest_whoop_if_fav_song_in_room_playlist(self):
        self.room_1.add_song_to_room_playlist(self.song1)
        self.room_1.check_in_guests_to_room(self.guest1)
        expected_value = "Whoop!"
        actual_value = self.guest1.whoop(self.room_1.playlist)
        self.assertEqual(expected_value, actual_value)
        print(expected_value)