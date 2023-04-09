import random

class URLCategory:
    def __init__(self, name: str, color=None):
        self.name = name
        if color is None:
            self.color = random.randint(0, 359)
        else:
            self.color = color

    def get_color(self):
        return self.color

    def get_category_name(self):
        return self.name

