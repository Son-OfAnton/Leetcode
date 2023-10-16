import random

class RandomizedSet:

    def __init__(self):
        self.idx = dict()
        self.keys = []

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False

        self.idx[val] = len(self.keys)
        self.keys.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False

        last_key, idx = self.keys[-1], self.idx[val]
        self.keys[idx] = last_key
        self.idx[last_key] = idx
        self.keys.pop()
        self.idx.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.keys)
