from Character import Character
from Talents import PlayerTalants
from Spell import SpellBook


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


class Player:
    def __init__(self, name):
        self.name = name
        self.character = Character()
        self.talents = PlayerTalants()
        self.action_bar = ActionBar()
        self.spell_book = SpellBook()

    def use_action(self, spell_name, target):
        self.spell_book[spell_name].use(self.character, target)

    def add_talent(self):
        pass

    def auto_attack(self):
        pass

    def add_target(self):
        pass

    def remove_target(self):
        pass
