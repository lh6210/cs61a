

class Celsius:
    def __init__(self, value):
        self.temperature = value

    @property
    def temperature(self):
        print('reading...')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('setting...')
        self._temperature = value

class miner:
    def __init__(self, value):
        self.v = value

    def __call__(self, k):
        return k - self.v


def cascade(n):
    print(n)
    if n < 10:
        return
    cascade(n // 10)
    print(n)
