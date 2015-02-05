from Attributes import CharacterAttributes


class AttributeBonus:
    def __init__(self, bonuses=None):
        self._bonuses = bonuses or {}

    def __getitem__(self, bonus_name):
        if bonus_name in self._bonuses:
            return self._bonuses[bonus_name]
        return 0

    def increase(self, bonus_name, amount):
        if amount < 0:
            return False
        if bonus_name in self._bonuses:
            self._bonuses[bonus_name] += amount
        else:
            self._bonuses[bonus_name] = amount
        return True

    def decrease(self, bonus_name, amount):
        if amount < 0:
            return False
        if bonus_name in self._bonuses:
            self._bonuses[bonus_name] -= amount
        else:
            self._bonuses[bonus_name] = -amount
        return True

    @property
    def get_all_bonuses(self):
        return self._bonuses


class StatCalculator:
    CALCULATION_VALUES = {
        'Health': {'Stamina': 3},
        'Mana': {'Intellect': 4},
        'AttackDamage': {'AttackPower': 0.4, 'AttackSpeed': 0.2},
        'AttackSpeed': {'Minuend': 3, 'AttackSpeed': 0.02},
        'CastSpeed': {'CastSpeed': 0.016, 'SpellPower': 0.001},
        'SpellDamage': {'SpellPower': 0.4, 'Intellect': 0.2}
        'Armor': {'Armor': 1}
    }

    def __init__(self, calculation_values):
        self.calculation_values = calculation_values

    def get(self, stat_name, bonuses, attributes):
        stat_parameters = self.CALCULATION_VALUES[stat_name]
        value = bonuses[stat_name]
        minuend = 0
        for parameter in stat_parameters:
            if parameter == 'Minuend':
                minuend = stat_parameters['Minuend']
            value += attributes[parameter] * stat_parameters[value]

        if minuend != 0:
            value = minuend - value

        return value


class TalentPoint:
    def __init__(self):
        self._free_points = 2
        self._used_points = 0

    def use_point(self):
        if self._free_points > 0:
            self._free_points -= 1
            self._used_points += 1

        return "{0} free points left".format(self._free_points)

    def release_points(self):
        if self._used_points > 0:
            self._free_points += self._used_points
            self._used_points = 0

    def add(self):
            self._free_points += 2


class Experience:
    def __init__(self):
        self._level = 1
        self._lvl_cap = 10
        self._xp_cap = 100
        self._xp = 0
        self._excess = 0

    def get_values(self):
        return(self._xp, self._xp_cap)

    def add(self, amount):

        self._xp += amount
        if self._xp >= self._xp_cap:
            self._excess = self._xp - self._xp_cap
            self._level = self.__increase_lvl()

        self._excess = 0
        return self._level

    def __increase_lvl(self):
        if self._level == self._lvl_cap:
            return self._level

        self._level += 1
        self._xp_cap = self._xp_cap*self._level
        self._xp = 0

        if self._excess > 0:
            self._level = self.add(self._excess)
        return self._level


class CharacterStats:
    def __init__(self):
        self.level = 1
        self.attributes = CharacterAttributes()
        self.experience = Experience()
        self.talent_points = TalentPoint()
        self.bonus = AttributeBonus()
        self.stats = StatCalculator()

    def add_bonus(self, name, amount):
        pass

    def add_experience(self, amount):
        if amount < 0:
            return False

        level = self.experience.add(amount)
        if self.level < level:
            self.__increase_level()
        return True

    def __increase_level(self):
        self.level += 1
        self.attributes.increase_level(self.level)
        self.talent_points.add()
        self.add_experience(0)

    def increase_attribute(self, attribute, amount):
        return self.attributes.increase(attribute, amount)

    def decrease_attribute(self, attribute, amount):
        return self.attributes.decrease(attribute, amount)

    def attr_value(self, attribute):
        return self.attributes[attribute]

    @property
    def get_xp(self):
        return self.experience.get_values()

    @property
    def max_health(self):
        return self.stats.get('Health', self.bonuses, self.attributes)

    @property
    def max_mana(self):
        return self.stats.get('Mana', self.bonuses, self.attributes)

    @property
    def attack_damage(self):
        return self.stats.get('AttackDamage', self.bonuses, self.attributes)

    @property
    def attack_speed(self):
        return self.stats.get('AttackSpeed', self.bonuses, self.attributes)

    @property
    def cast_speed(self):
        return self.stats.get('CastSpeed', self.bonuses, self.attributes)

    @property
    def spell_damage(self):
        return self.stats.get('SpellDamage', self.bonuses, self.attributes)

    @property
    def armor(self):
        return self.stats.get('Armor', self.bonuses, self.attributes)
