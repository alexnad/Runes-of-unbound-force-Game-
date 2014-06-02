from Attributes import Attribute, TalentPoint, Experience, 
                        CharacterAttributes, CharacterStats





class PlayerTalants:
    def __init__(self, primary):
        self.primary = primary
        self.boosted = primary
        self.talent_tree = None
        

    def add_talent(self, talent):
        if talent in self.talent_tree:
            return(talent_tree.use_point(talent ,self.primary, self.boosted))
        return False

    def reset_talent_tree(self):
        self.talent_tree.reset()
        self.talent_tree = None

    def choose_talent_tree(self, tree):
        if talent_tree != None
            self.reset_talent_tree()
        talent_tree = tree

    



class Spell(threading.Thread):
    def __init__(self, damage, target):
       self.damage = damage
       self.target = target
       threading.Thread.__init__(self)
    def run(self):
       self.target -= self.damage
       return self.target
