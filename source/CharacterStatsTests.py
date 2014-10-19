import unittest
from CharacterStats import AttributeBonus, TalentPoint, Experience
from CharacterStats import CharacterStats


class TestAttributeBonus(unittest.TestCase):
    def setUp(self):
        self.bonus = AttributeBonus()

    def test_if_bonus_dict_is_empty_after_initialisation(self):
        self.assertFalse(self.bonus.get_all_bonuses)

    def test_increase_bonus(self):
        self.assertEqual(self.bonus['AttackSpeed'], 0)
        self.bonus.increase('AttackSpeed', 20)
        self.assertTrue(self.bonus.increase('AttackSpeed', 20))
        self.assertEqual(self.bonus['AttackSpeed'], 40)
        self.assertFalse(self.bonus.increase('AttackSpeed', -20))

    def test_decrease_bonus(self):
        self.bonus.decrease('Stamina', 20)
        self.assertTrue(self.bonus.decrease('Stamina', 20))
        self.assertEqual(self.bonus['Stamina'], -40)
        self.assertFalse(self.bonus.decrease('Stamina', -20))


class TestTalentPoint(unittest.TestCase):
    def setUp(self):
        self.points = TalentPoint()

    def test_initialisation(self):
        self.assertEqual(self.points._free_points, 2)
        self.assertEqual(self.points._used_points, 0)

    def test_use_point(self):
        self.assertEqual(self.points.use_point(), '1 free points left')

    def test_add_points(self):
        self.points.add()
        self.assertEqual(self.points._free_points, 4)

    def test_release_points(self):
        self.points.use_point()
        self.points.use_point()
        self.points.release_points()
        self.assertEqual(self.points._free_points, 2)


class TestExpirience(unittest.TestCase):
    def setUp(self):
        self.exp = Experience()

    def test_new_talent_point_initialisation(self):
        self.assertEqual(self.exp._level, 1)
        self.assertEqual(self.exp._lvl_cap, 10)
        self.assertEqual(self.exp._xp_cap, 100)
        self.assertEqual(self.exp._xp, 0)
        self.assertEqual(self.exp._excess, 0)

    def test_add_exp(self):
        self.assertEqual(self.exp.add(40), 1)
        self.assertEqual(self.exp._xp, 40)

    def test_increase_level(self):
        self.assertEqual(self.exp.add(101), 2)
        self.assertEqual(self.exp._xp, 1)
        self.assertEqual(self.exp._xp_cap, 200)
        self.assertEqual(self.exp._excess, 0)

    def test_add_increse_level_recursion(self):
        self.assertEqual(self.exp.add(90001), 7)
        self.assertEqual(self.exp._xp, 2701)
        self.assertEqual(self.exp._xp_cap, 504000)
        self.assertEqual(self.exp._excess, 0)

    def test_level_cap_reach(self):
        self.assertEqual(self.exp.add(40911301), 10)


class TestCharacterStats(unittest.TestCase):
    def setUp(self):
        self.character = CharacterStats()

    def test_add_expirience(self):
        self.character.add_experience(50)
        self.assertFalse(self.character.add_experience(-1))
        self.assertEqual(self.character.get_xp[0], 50)
        self.assertEqual(self.character.level, 1)

    def test_increase_level(self):
        self.assertTrue(self.character.add_experience(101))
        self.assertEqual(self.character.level, 2)

    def test_add_expirience_and_increase_level_recursion(self):
        self.assertTrue(self.character.add_experience(301))
        self.assertEqual(self.character.get_xp[0], 1)
        self.assertEqual(self.character.get_xp[1], 600)

    def test_increase_arttribute(self):
        self.assertTrue(self.character.increase_attribute('Stamina', 50))
        self.assertEqual(self.character.attr_value('Stamina'), 120)

    def test_decrease_value(self):
        self.assertTrue(self.character.decrease_attribute('Stamina', 20))
        self.assertEqual(self.character.attr_value('Stamina'), 50)

if __name__ == "__main__":
    unittest.main()
