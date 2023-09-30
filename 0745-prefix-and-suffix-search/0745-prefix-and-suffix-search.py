class TrieNode:
    
    def __init__(self):
        
        self.is_end = False
        self.children = dict()
        self.indexes = []

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str, idx: int) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.indexes.append(idx)
        curr.is_end = True


    def starts_with(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        return curr.indexes

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_trie, self.suffix_trie = Trie(), Trie()

        for i, word in enumerate(words):
            self.prefix_trie.insert(word, i)
            self.suffix_trie.insert(word[::-1], i)
        
    def f(self, pref: str, suff: str) -> int:
        prefix_list = self.prefix_trie.starts_with(pref)
        suffix_list = self.suffix_trie.starts_with(suff[::-1])
        i, j = len(prefix_list) - 1, len(suffix_list) - 1

        while i >= 0 and j >= 0:
            if prefix_list[i] == suffix_list[j]:
                return prefix_list[i]
            elif prefix_list[i] > suffix_list[j]:
                i -= 1
            else:
                j -= 1

        return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)