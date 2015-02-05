import unittest
from encounters import NPC


class Character:
    pass


class TestNPC(unittest.TestCase):
    def setUP(self):
        self.animal = NPC('alpha wolf', 'beast')

    def test_valid_target(self):
        test_target_NPC = NPC('bird', 'beast')
        test_target_character = Character()
        self.assertFalse(self.animal.valid_target(test_target_NPC))
        #self.assertFalse(self.animal.valid_target(test_target_character))
