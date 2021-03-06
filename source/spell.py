# import time


class Spell:
    def __init__(self, cast_time, damage, healing, mana_cost):
        self.cast_time = cast_time
        self.damage = damage
        self.healing = healing
        self.mana_cost = mana_cost

    def cast(self, attacker, victime):
        attacker.remove_mana(self.mana_cost)
        if attacker.is_friendly(victime):
            self.positive_effect(victime)
        else:
            self.negative_effect(victime)

    def negative_effect(self, victime):
        victime.remove_health(self.damage)

    def positive_effect(self, victime):
        victime.add_health(self.healing)
"""

class FireBall:
    def __init__(self):
        self.cast_time = 3
        self.damage = 150

    def cast_time(self, character, target):
        return self.cast_time - character.cast_speed

    def damage(self, character, target):
        pass

    def cast(self, character, target):
        cast_time = cast_time(character, target)
        time.sleep(self.cast_time)
        target.inflict_damage(self.damage(character, target))


class SoulLeak:
    def __init__(self, character, target):
        self.damage = 10
        self.duration = 10
        self.effect = Effects('boost_SP', 1, 10)

    def cast(self, target):
        target.damage_over_time(self.damage, self.duration)
        target.add_effect()


class Bash:
    def __init__(self):
        self.bash_time = 3

    def effect(self, character, target):
        target.impare(self.bash_time)


class SpellBook:
    def __init__(self):
        self.content = {}

    def add_spell(self, spell):
        if spell['name'] not in self.content:
            self.content[spell['name']] = spell['object']
        else:
            return 'spell already in spellbook'

    def remove_spell(self, spell):
        if spell

class StatCondition:
    def __init__(self, stats):
        pass


class StatPool:
    def __init__(self, stat):
        self.stat = stat


class CharaterCondition:
    def __init__(self, character):
        self.stats = character.stats
        self.health_pool = self.stats.max_health
        self.mana_pool = self.stats.max_mana

    def auto_attack(self):
        pass

    def add_effect(self, effect):
        pass

    def take_spell(self, spell):
        pass

    def take_curse(self, curse):
        pass

    def take_buff(self, buff):
        pass

    def take_damage(self, damage):
        pass


class DamageOverTime():
    def __init__(self, damage, duration, interval=1):
        self.damage = damage
        self.duration = duration
        self.interval = interval

    def effect(self, target):
        for x in range(self.duration):
            time.sleep(self.interval)
            target.stat_pool('health').decrease(self.damage)


EFFECTS = {'DoT': DamageOverTime}


class Effect():
    def __init__(self, name, target, type, *args):
        self.name = name
        self.target = target
        self.type = EFFECTS[type](*args)

    def run(self):
        self.type.effect(self.target)

"""
