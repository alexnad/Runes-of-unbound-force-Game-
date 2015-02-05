from Character import Character


class Player:
    def __init__(self, name):
        self.name = name
        self.character = Character()

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
