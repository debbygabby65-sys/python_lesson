import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from main import play_game

class TestMysteryIsland(unittest.TestCase):
    def test_starting_energy(self):
            
