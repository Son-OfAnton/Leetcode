class MyHashMap:

    def __init__(self):
        self.hash_table = [None]*(pow(10, 6) + 1)
        self.MOD = pow(10, 9) + 7

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.MOD
        self.hash_table[hash_key] = value

    def get(self, key: int) -> int:
        hash_key = key % self.MOD
        if self.hash_table[hash_key] == None:
            return -1
        else:
            return self.hash_table[hash_key]
        

    def remove(self, key: int) -> None:
        hash_key = key % self.MOD
        self.hash_table[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)