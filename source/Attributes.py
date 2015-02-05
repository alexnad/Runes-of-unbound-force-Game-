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
    LEVEL_BONUSES = {
        'Stamina': 5,
        'Intellect': 6,
        'AttackSpeed': 2,
        'CastSpeed': 2,
        'AttackPower': 8,
        'SpellPower': 8,
        'Armor': 10
    }

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

    def level_bonus(self, level, attribute):
        return level * self.LEVEL_BONUSES[attribute]

    def increase_level(self, level):
        for attribute in self.attributes:
            increase_amount = self.level_bonus(level, attribute)
            self.increase(attribute, increase_amount)
