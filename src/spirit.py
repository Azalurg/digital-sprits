import png
import src.mixer as mixer


def generate(mask, key, name, color_amount=3):
    img = []
    width = len(mask[0])
    height = len(mask)
    use_colors = False
    colors = {}
    if color_amount > 0:
        use_colors = True
        for i in range(2, color_amount + 2):
            r, key = key % 256, mixer.get(key)
            g, key = key % 256, mixer.get(key)
            b, key = key % 256, mixer.get(key)
            colors[i] = {"base": (r, g, b, 255), "current": (r, g, b, 255)}

    for y in range(height):
        row = ()
        for x in range(width):
            color, key = _get_color(mask[y][x], key, use_colors, colors)
            row += color
        img.append(row)

    img, width, height = _mirror_horizontally(img, width, height)

    with open(f'./images/{name}.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False, alpha=True, bitdepth=8)
        w.write(f, img)
    return 0


def _get_color(state, key, use_colors=False, colors=None):
    color = ()
    if state == -1:
        color = (0, 0, 0, 0)
    elif state == 0:
        color = (0, 0, 0, 255)
    elif state == 1:
        color = (255, 255, 255, 255)
    elif use_colors:
        color = colors[state]["current"]
        colors, key = _shift_colors(state, colors, key)
    else:
        r, key = key % 256, mixer.get(key)
        g, key = key % 256, mixer.get(key)
        b, key = key % 256, mixer.get(key)
        color = (r, g, b, 255)

    return color, key


def _mirror_horizontally(img, width, height):
    new_img = []
    for y in range(len(img)):
        row = img[y]
        for x in range(len(img[y]) - 1, 0, -4):
            row = row + (img[y][x - 3], img[y][x - 2], img[y][x - 1], img[y][x])
        new_img.append(row)
    return new_img, width * 2, height


def _shift_colors(color, colors, key):
    r, key = (colors[color]["current"][0] + key % 2) % 256, mixer.get(key)
    g, key = (colors[color]["current"][1] + key % 2) % 256, mixer.get(key)
    b, key = (colors[color]["current"][2] + key % 2) % 256, mixer.get(key)
    colors[color]["current"] = (r, g, b, 255)
    return colors, key
