class Counter:
    def __init__(self):
        self._count = 0

    def add(self):
        self._count += 1

    def get_count(self):
        return self._count