from Attributes import CharacterAttributes


class AttributeBonus:
    def __init__(self):
        self.bonuses = {}

    def __getitem__(self, bonus_name):
        return self.bonuses[bonus_name]

    def increase(self, bonus_name, amount):
        self.bonuses[bonus_name] += amount

    def decrease(self, bonus_name, amount):
        self.bonuses[bonus_name] -= amount


class TalentPoint:
    def __init__(self):
        self.free_points = 1
        self.used_points = 0

    def use_point(self):
        if self.free_points > 0:
            self.free_points -= 1
            self.used_points += 1
            return "{0} free points left".format(self.free_points)
        else:
            return "No free points left"

    def release_points(self):
        if self.used_points > 0:
            self.free_oints += self.used_points
            self.used_oints = 0

    def add(self, level):
        if level > 2:
            self.free_points += 2
        else:
            self.free_points += 1


class Experience:
    def __init__(self):
        self.level = 1
        self.level_cap = 10
        self.experience_cap = 100
        self.experience = 0
        self.excess = 0

    def add(self, amount):
        self.experience += amount
        if self.experience >= self.experience_cap:
            self.excess = self.experience - self.experience_cap
            self.level = self.increse_lvl()

        self.excess = 0
        return self.level

    def increase_lvl(self):
        if self.level == self.level_cap:
            return self.level

        self.level += 1
        self.experience_cap = self.experience_cap*self.level
        self.experience = 0

        if self.excess > 0:
            self.level = self.add_experience(self.excess)
        return self.level


class CharacterStats:
    def __init__(self):
        self.level = 1
        self.attributes = CharacterAttributes()
        self.experience = Experience()
        self.talent_points = TalentPoint()

    def add_experience(self, amount):
        level = self.experience.add(amount)
        if self.level < level:
            self.increase_level()

    def increase_level(self):
        self.level += 1
        self.attributes.increase_level(self.level)
        self.talent_points.add(self.level)
        self.add_experience(0)

    def increase_attribute(self, attribute, amount):
        self.attributes.increase(attribute, amount)

    def decrease_attribute(self, attribute, amount):
        self.attributes.decrease(attribute, amount)

    def get_attribute_value(self, attribute):
        return self.attributes.get_value(attribute)

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
