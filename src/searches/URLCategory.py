import random


def generate_pastel_color():
    # Generate random RGB values
    r = random.uniform(0.5, 1)
    g = random.uniform(0.5, 1)
    b = random.uniform(0.5, 1)
    # Convert to a pastel color by averaging the RGB values with white
    pastel = (r + 1) / 2, (g + 1) / 2, (b + 1) / 2
    # Convert the RGB values to hex
    hex_color = '#' + ''.join(hex(int(c * 255))[2:].zfill(2) for c in pastel)
    return hex_color


class URLCategory:
    def __init__(self, name: str, color=None):
        self.name = name
        if color is None:
            self.color = generate_pastel_color()
        else:
            self.color = color


    def getColor(self):
        return self.color

    def getCategoryName(self):
        return self.name

