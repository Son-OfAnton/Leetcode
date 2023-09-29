class TrieNode:

    def __init__(self):
        self.children = dict()
        self.is_end = False
        self.val = 0
        self.prev_val  = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        key_exists = False
        curr = self.root

        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        key_exists = curr.is_end
        diff = val - curr.prev_val
        curr.prev_val = val

        if key_exists:
            curr = self.root

            for char in key:
                curr = curr.children[char]
                curr.val += diff
        else:
            curr = self.root
            for char in key:
                curr = curr.children[char]
                curr.val += val

            curr.is_end = True


    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char] 
        return curr.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)