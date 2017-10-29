class Room(object):
    # only allow certain paths to be followed by player


    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

class Human(object):

    # Hp stands for hit points. style = fighting style i.e. fighter or wizard
    def __init__(self, name, current_hp, max_hp):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.style = {}

        # combat of fighting style
    def update_style(self, combat):
        return self.style.get(combat, None)

    def add_style(self, style):
        self.style.update(style)
