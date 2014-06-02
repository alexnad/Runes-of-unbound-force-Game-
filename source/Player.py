import unittest
from Character


class ActionBar:
    def __init__(self):
        self.volume = 8
        self.content = {}

    def add_action(self, action, place):
        if len(self.content) < volume
            self.content[place] = action

    def remove_action(self, place):
        del self.content[place]

    def use_action(self, place, target = None):
        self.content[place].use(target)



class Player:
    def __init__(self, name):
        self.name = name
        self.character = Character()
        self.talents = Talents()
        self.action_bar = ActionBar()
        self.spell_book = SpellBook()
    
    def use_action(self, spell_name, target):
        spell_book[spell_name].use(self.character ,target)

    def add_talent(self):
        
    def auto_attack(self):

    def add_target(self):

    def remove_target(self):
