def get(key: int):
    return (key * 353056231445948244643703619017) % 31976341530616062225701619174238451


def hash_gen(mask, length=8):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    control_sum = 0
    for y in range(len(mask)):
        for x in range(len(mask[y])):
            control_sum += mask[y][x]

    result = ''
    for i in range(length):
        result += alphabet[control_sum % len(alphabet)]
        control_sum = get(control_sum)
    return result
