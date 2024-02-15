from typing import List

from src.mixer import Mixer


class Mask:
    def __init__(
        self, width: int, height: int, colors: int, transparency=False, axes=1, salt=1
    ):
        self.mixer = Mixer()
        self.mask = []
        self.width = width
        self.height = height
        self.transparency = transparency
        self.axes = axes
        self.colors_list = [0, 1]
        self.salt = salt
        self.name = ""

        if transparency:
            self.colors_list.append(-1)

        for i in range(2, colors + 2):
            self.colors_list.append(i)

        self.colors = len(self.colors_list)

    def generate(self):
        if self.axes == 0:
            for x in range(self.height):
                row = []
                for y in range(self.width):
                    row.append(self.mixer.choice(self.colors_list, self.salt))
                self.mask.append(row)

        if self.axes == 1:
            for x in range(self.height):
                row = []
                self.width = (self.width // 2) * 2
                for y in range(self.width // 2):
                    number = self.mixer.choice(self.colors_list, self.salt)
                    row.insert(y, number)
                    row.insert(-1 - y, number)
                self.mask.append(row)

        self.name = self.mixer.hash64(self.mask)
