import unittest
from Attributes import Attribute, TalentPoint, CharacterStats


class Empower:
    def __init__(self):
        self.description = "Increses your attack power by 10/20/30%."
        self.points = 3
        self.boost_amount = 0
        self.boost_percentige = 0
    

    def calculate_boost_amount(self, primary):
        attack_power_value = primary.attribute_value('AttackPower')
        self.boost_amount = attack_power_value * self.boost_percentige
        

    def undo_boost(self, boosted):
        boosted.decrease_attribute('AttackPower', self.boost_amount)
        boost_amount = 0

    def free_points_left():
        return self.points > 0        

    def boost(self, primary, boosted):
        self.calculate_boost_value(primary)
        boosted.increase_attribute('AttackPower', self.boost_amount)

    def reboost(self, primary, boosted):
        self.undo_boost(boosted)
        self.boost(primary, boosted)

    def add_point(self, primary, boosted):
        if self.free_points_left():
            self.free_points -= 1
            self.undo_boost(boosted)
            self.boost_percentige += 0.10
            calculate_boost_amount(primary)
            self.boost(primary, boosted)
            return True

        return False


    def release_points(self, boosted):
        self.undo_boost(boosted)
        self.boost_percentige = 0
        self.points = 3



class SwiftBlade:
    def __init__(self):
        self.description = "Increases you attack speed by 10/15/20%"
        self.points = 3
        self.boost_amount = 0
        self.boost_percentige = 0.05

    def calculate_boost_amount(self, primary):
        attack_speed_value = primary.attribute_value('AttackSpeed')
        self.boost_amount = attack_speed_value * self.boost_percentige
        

    def undo_boost(self, boosted):
        boosted.decrease_attribute('AttackSpeed', self.boost_amount)
        boost_amount = 0

    def free_points_left():
        return self.points > 0        

    def boost(self, primary, boosted):
        self.calculate_boost_value(primary)
        boosted.increase_attribute('AttackSpeed', self.boost_amount)

    def reboost(self, primary, boosted):
        self.undo_boost(boosted)
        self.boost(primary, boosted)

    def add_point(self, primary, boosted):
        if self.free_points_left():
            self.free_points -= 1
            self.undo_boost(boosted)
            self.boost_percentige += 0.05
            calculate_boost_amount(primary)
            self.boost(primary, boosted)
            return True

        return False


    def release_points(self, boosted):
        self.undo_boost(boosted)
        self.boost_percentige = 0.05
        self.points = 3


class CriticalStike:
    def __init__(self):
        self.description = 
                    "Your abilities have a chance of dealing 2X normal damage"
        self.point = 1

    def boost(self, boosted):
        boosted.critical_strike = True

    def undo_boost(self, boosted):
        boosted.critical_strike = False

    def free_points_left():
        return self.points > 0   
    
    def add_point(self, primary, boosted):
        if free_points_left():
            self.boost(boosted)
            self.points -= 1
            return True
        return False

    def release_points(self, boosted):
        self.undo_boost(boosted)
        self.points = 1


class DeepCut:



class ArmsTree:
    def __init__(self):
        self.tree = {'Empower': Empower(), 'Swift Blade': SwiftBlade(),
                     'Critical Strike': CriticalStike()}

    def __getitem__(self, talent):
        return self.tree[talent]

    def __contains__(self, talent):
        return talent in self.tree

    def use_point(self, talent, primary, boosted):
        return self.tree[talent].add_point(primary, boosted)
        
    def reset(self, boosted):
        for talent in self.tree:
            talent.release_points(boosted)

    def add_points()


    
