ATTRIBUTE_VALUES = {
    'Stamina': 70,
    'Intellect': 60,
    'AttackSpeed': 40,
    'AttackPower': 120,
    'SpellPower': 120,
    'CastSpeed': 40,
    'Armor': 150
}


class Attribute:
    def __init__(self):
        self.name = self.__class__.__name__
        self.attr_value = ATTRIBUTE_VALUES[self.name]

    def increase(self, amount):
        if amount < 0:
            return False
        self.attr_value += amount
        return True

    def decrease(self, amount):
        if amount < 0:
            return False
        self.attr_value -= amount
        return True

    @property
    def value(self):
        return self.attr_value


class CharacterAttributes:
    def __init__(self):
        self.attributes = {key: type(key, (Attribute,), {})() for key
                           in ATTRIBUTE_VALUES}

    def __getitem__(self, attr_name):
        if attr_name in self.attributes:
            return self.attributes[attr_name].value
        return 0

    def increase(self, name, amount):
        return self.attributes[name].increase(amount)

    def decrease(self, name, amount):
        return self.attributes[name].decrease(amount)

    def increase_level(self, level):
        self.increase('Stamina', level*5)
        self.increase('Intellect', level*6)
        self.increase('AttackSpeed', level*2)
        self.increase('CastSpeed', level*2)
        self.increase('AttackPower', level*8)
        self.increase('SpellPower', level*8)
        self.increase('Armor', level*10)
