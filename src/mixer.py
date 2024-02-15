class Mixer:
    _key = 8194907056147789

    def random(self, salt=0):
        self._key = (
            self._key * 53854986464371996139 + 19882310927922663229 + salt
        ) % 6543547642338880518018439
        return self._key

    def choice(self, data: list, salt=0):
        data_range = len(data)
        return data[self.random(salt) % data_range]

    def hash64(self, mask):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        control = 1
        for y in range(len(mask)):
            small_sum = 0
            for x in range(len(mask[y])):
                small_sum += mask[y][x]

            if small_sum > 0:
                control *= small_sum

        result = ""
        for i in range(64):
            result += alphabet[control % len(alphabet)]
            control = self.random(salt=control)
        return result
