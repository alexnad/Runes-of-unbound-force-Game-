import unittest
from Attributes import CharacterAttributes


class TestCharacterAttributes(unittest.TestCase):
    def setUp(self):
        self.character = CharacterAttributes()

    def test_attribute_values(self):
        self.assertEqual(self.character['Stamina'], 70)
        self.assertEqual(self.character['Intellect'], 60)
        self.assertEqual(self.character['AttackSpeed'], 40)
        self.assertEqual(self.character['AttackPower'], 120)
        self.assertEqual(self.character['SpellPower'], 120)
        self.assertEqual(self.character['CastSpeed'], 40)
        self.assertEqual(self.character['Armor'], 150)

    def test_increase_attribute(self):
        self.assertTrue(self.character.increase('Stamina', 50))
        self.assertEqual(self.character['Stamina'], 120)
        self.assertFalse(self.character.increase('Stamina', -20))

    def test_decrease_attribute(self):
        self.assertTrue(self.character.decrease('Stamina', 20))
        self.assertEqual(self.character['Stamina'], 50)
        self.assertFalse(self.character.decrease('Stamina', -20))

    def test_increase_level(self):
        self.character.increase_level(2)

        self.assertEqual(self.character['Stamina'], 80)
        self.assertEqual(self.character['Intellect'], 72)
        self.assertEqual(self.character['AttackSpeed'], 44)
        self.assertEqual(self.character['CastSpeed'], 44)
        self.assertEqual(self.character['AttackPower'], 136)
        self.assertEqual(self.character['SpellPower'], 136)
        self.assertEqual(self.character['Armor'], 170)
        self.assertEqual(self.character['baba'], 0)

if __name__ == "__main__":
    unittest.main()
