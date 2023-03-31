import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
       self.song1 = Song("Simply The Best", "Tina Turner")