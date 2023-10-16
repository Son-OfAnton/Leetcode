import random

class RandomizedSet:

    def __init__(self):
        self.table = dict()
        self.keys = []

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False

        self.table[val] = len(self.keys)
        self.keys.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False

        last_key, idx = self.keys[-1], self.table[val]
        self.keys[idx] = last_key
        self.table[last_key] = idx
        self.keys.pop()
        self.table.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.keys)
