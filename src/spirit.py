import png
from src.mask import Mask
from src.mixer import Mixer


class Spirit:
    img = []
    colors = {0: (0, 0, 0, 255), 1: (255, 255, 255, 255), -1: (0, 0, 0, 0)}
    mixer = Mixer()

    def __init__(self, mask: Mask):
        self.mask = mask

        self.generate()
        self.save()

    def generate(self):
        for color in self.mask.colors_list:
            if color in [-1, 0, 1]:
                continue
            r = self.mixer.random() % 256
            g = self.mixer.random() % 256
            b = self.mixer.random() % 256
            self.colors.setdefault(color, (r, g, b, 255))

        for y in range(self.mask.height):
            row = ()
            for x in range(self.mask.width):
                color = self.colors.get(self.mask.mask[y][x], (255, 0, 255, 255))
                row += color
            self.img.append(row)
            self._shift_colors()

    def save(self):
        with open(f"./images/{self.mask.name}.png", "wb") as f:
            w = png.Writer(
                self.mask.width,
                self.mask.height,
                greyscale=False,
                alpha=True,
                bitdepth=8,
            )
            w.write(f, self.img)
        return 0

    def _shift_colors(self):
        for key, value in self.colors.items():
            if key in [-1, 0, 1]:
                continue
            new_color = (
                (value[0] + self.mixer.random() % 2) % 256,
                (value[1] + self.mixer.random() % 2) % 256,
                (value[2] + self.mixer.random() % 2) % 256,
                255,
            )

            self.colors[key] = new_color
