import src.mixer as mixer


def generate(key, width=8, height=16, transparency=False, color_amount=3):
    numbers = [0, 1]
    if transparency:
        numbers.append(-1)

    for i in range(2, color_amount+2):
        numbers.append(i)

    numbers_amount = len(numbers)

    mask = []
    for y in range(height):
        row = []
        for x in range(width):
            n, key = numbers[key % numbers_amount], mixer.get(key)
            row.append(n)
        mask.append(row)

    return mask, key
