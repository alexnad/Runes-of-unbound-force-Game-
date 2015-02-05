import unittest
from spell import Spell, AoESpell


class Character:
    def __init__(self, health, mana, fraction):
        self.health = health
        self.mana = mana
        self.fraction = fraction

    def add_health(self, amount):
        self.health += amount

    def add_mana(self, amount):
        self.mana += amount

    def remove_health(self, amount):
        self.health -= amount

    def remove_mana(self, amount):
        self.mana -= amount

    def is_friendly(self, target):
        if self.fraction == target.fraction:
            return True
        return False


class TestSpell(unittest.TestCase):
    def setUp(self):
        self.spell = Spell(0, 200, 200, 200)
        self.caster = Character(1000, 1000, 'Horde')
        self.victime = Character(1000, 1000, 'Aliance')
        self.health_spell_on_caster = 1200
        self.mana_after_cast = 800
        self.health_spell_on_target = 800

    def test_spell_on_self(self):
        self.spell.cast(self.caster, self.caster)
        self.assertEqual(self.caster.health, self.health_spell_on_caster)
        self.assertEqual(self.caster.mana, self.mana_after_cast)

    def test_spell_on_victime(self):
        self.spell.cast(self.caster, self.victime)
        self.assertEqual(self.caster.mana, self.mana_after_cast)
        self.assertEqual(self.victime.health, self.health_spell_on_target)


class TestAoESpell(unittest.TestCase):
    def setUp(self):
        spell = AoESpell(0, 100, 100, 600)
        self.caster = Character(1000, 1000, 'Horde')
        self.ally = Character(1000, 1000)


if __name__ == "__main__":
    unittest.main()
