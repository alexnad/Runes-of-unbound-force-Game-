from Attributes import CharacterAttributes


class AttributeBonus:
    def __init__(self):
        self._bonuses = {}

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
        return (self.experience._xp, self.experience._xp_cap)

    @property
    def max_health(self):
        return self.attributes['Stamina'].value*3 + self.bonus['health']

    @property
    def max_mana(self):
        return self.attributes['Intellect'].value*4 + self.bonus['mana']

    @property
    def attack_damage(self):
        return self.attributes['AttackPower'].value/3 + self.bonus['damage']

    @property
    def attack_speed(self):
        return 2 - self.attributes['AttackSpeed'].value/160\
            + self.bonus['attack_speed']

    @property
    def cast_speed(self):
        return self.attributes['CastSpeed'].value/200\
            + self.bonus['cast_speed']

    @property
    def spell_damage(self):
        return self.attributes['SpellPower'].value/3\
            + self.attributes['Intellect'].value/6 + self.bonus['spell_damage']

    @property
    def armor(self):
        return self.attributes['Armor'].value + self.bonus['armor']
