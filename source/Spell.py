import time


class Spell(threading.Thread):
    def __init__(self, damage, target):
       self.damage = damage
       self.target = target
       threading.Thread.__init__(self)
    def run(self):
       self.target -= self.damage
       return self.target



class FireBall:
    def __init__(self):
        self.cast_time = 3
        self.damage = 150
    
    def cast_time(self , character, target):
        return self.cast_time - character.cast_speed

    def damage(self, character, target):
        if(criticalstrike):
            a = 2
        return self.damage + character.spell_damage
    
    #@move
    def cast(self, character, target):
        cast_time = cast_time(character, target)
        time.sleep(cast_time)
        target.inflict_damage(self.damage(character, target))


class Effects:
    def __init__(self, name, value, duration):
        effect = 


class SoulLeak:
    def __init__(self, character, target):
        self.damage = 10
        self.duration = 10
        effect = Effects('boost_SP', 1, 10)

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


class StatCondition:
    def __init__(self, stats):


class StatPool:
    def __init__(self, stat):
        self. = stat

BattleStance

class CharaterCondition:
    def __init__(self, character):
        self.stats = character.stats
        self.health_pool = self.stats.max_health
        self.mana_pool = self.stats.max_mana
    
    def auto_attack(self):
        
    def add_effect(self, effect):
                


    def take_spell(self, spell):

    def take_curse(self, curse):

    def take_buff(self, buff):

    def take_damage(self, damage):



class DamageOverTime:
    def __init__(self, damage, duration, interval = 1):
        self.damage = damage
        self.duration = duration
        self.interval = interval

    def 


class Effect:
    def __init__(self, name, type, *args):
        self.name = name

        