from CharacterStats import CharacterStats
from Talents import PlayerTalants
from 

"""
class BasicAttack:
    def __init__(self, stats):
        self.damage = stats.attack_damage
        self.attack_speed = stats.attack_speed

    def calculate_attack_data(self, stats, weapon):
        self.damage = stats.attack_damage + weapon.damage

    def auto_attack(self, stats, weapon, target):
        while target:
            self.calculate_attack_data(stats, weapon)
            target.inflict(self.damage)
            time.sleep(attack_speed)
"""


class ActionBar:
    def __init__(self):
        self.volume = 8
        self.content = {}

    def add_action(self, action, place):
        if len(self.content) < self.volume:
            self.content[place] = action

    def remove_action(self, place):
        del self.content[place]

    def use_action(self, place, target=None):
        self.content[place].use(target)


class ActiveEffects:
    def __init__(self):
        pass


class Character:
    def __init__(self, name):
        self.stats = CharacterStats()
        self.active_effects = ActiveEffects()
        self.talents = PlayerTalants()
        self.action_bar = ActionBar()
        self.spell_book = SpellBook()
