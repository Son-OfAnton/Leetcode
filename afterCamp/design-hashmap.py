class MyHashMap:

    def __init__(self):
        self.hash_table = [None]*(pow(10, 6) + 1)

    def put(self, key: int, value: int) -> None:
        self.hash_table[key] = value

    def get(self, key: int) -> int:
        if self.hash_table[key] == None:
            return -1
        else:
            return self.hash_table[key]
        

    def remove(self, key: int) -> None:
        self.hash_table[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)