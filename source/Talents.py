from Character import Character


class PlayerTalants:
    def __init__(self, primary):
        self.primary = Character()
        self.boosted = primary
        self.talent_tree = None

    def add_talent(self, talent):
        if talent not in self.talent_tree:
            return False

        return(self.talent_tree.use_point(talent, self.primary, self.boosted))

    def reset_talent_tree(self):
        self.talent_tree.reset()
        self.talent_tree = None

    def choose_talent_tree(self, tree):
        if self.talent_tree is not None:
            self.reset_talent_tree()
        self.talent_tree = tree
