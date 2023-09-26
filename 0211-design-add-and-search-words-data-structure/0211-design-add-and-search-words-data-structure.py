class TrieNode:
    
    def __init__(self, val='*'):
        self.val = val
        self.children = dict()
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True
        

    def search(self, word: str, curr: TrieNode=None) -> bool:
        if curr == None:
            curr = self.root
        for i, char in enumerate(word):
            if char == '.':
                for c in curr.children:
                    if self.search(word[i+1:], curr.children[c]):
                        return True
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.is_end
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)