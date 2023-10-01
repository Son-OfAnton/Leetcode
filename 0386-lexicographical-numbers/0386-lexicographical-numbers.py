class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(current, result):
            if current > n:
                return
            if current != 0:  
                result.append(current)
            
            for i in range(10):
                if current * 10 + i > n:
                    return
                dfs(current * 10 + i, result)
                
        result = []
        for i in range(1, 10):
            dfs(i, result)
        
        return result

"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 10
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        num_str = str(num)

        for char in num_str:
            digit = int(char)
            if curr.children[digit] is None:
                curr.children[digit] = TrieNode()
            curr = curr.children[digit]

        curr.is_end = True

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num_trie = Trie()
        for num in range(1, n + 1):
            num_trie.insert(num)

        def dfs(node, num):
            if node.is_end:
                lexically_sorted_nums.append(num)

            for digit in range(10):
                child = node.children[digit]
                if child is not None:
                    dfs(child, num * 10 + digit)

        lexically_sorted_nums = []
        for num in range(1, 10):
            node = num_trie.root.children[num]
            if node is not None:
                dfs(node, num)

        return lexically_sorted_nums

"""