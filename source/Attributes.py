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
        self.value = ATTRIBUTE_VALUES[self.__class__.__name__]

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount

    @property
    def value(self):
        return self.value


class CharacterAttributes:
    def __init__(self):
        self.attributes = {key: type(key, (Attribute,), {})() for key
                           in ATTRIBUTE_VALUES.keys()}

    def __getitem__(self, attr_name):
        return self.attributes[attr_name]

    def increase(self, name, amount):
        self.attributes[name].increase(amount)

    def decrease(self, name, amount):
        self.attributes[name].increase(amount)

    def value(self, name):
        return self.attributes[name].value

    def increase_per_level(self, level):
        self.increase('Stamina', level*5)
        self.increase('Intellect', level*6)
        self.increase('AttackSpeed', level*2)
        self.increase('CastSpeed', level*2)
        self.increase('AttackPower', level*8)
        self.increase('SpellPower', level*8)
        self.increase('Armor', level*10)
