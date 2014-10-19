from CharacterStats import CharacterStats
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


class ActiveEffects:
    def __init__(self):
        pass


class Character:
    def __init__(self, name):
        self.stats = CharacterStats()
        self.active_effects = ActiveEffects
        self.name = name
