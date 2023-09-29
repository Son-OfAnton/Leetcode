class TrieNode:
    
    def __init__(self):
        
        self.is_end = False
        self.children = dict()
        self.count = 0
        

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        score = 0
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
        curr.is_end = True
        


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        dictionary = Trie()
        scores = []
        
        for word in words:
            dictionary.insert(word)
        
        for word in words:
            curr = dictionary.root
            score = 0
            for char in word:
                curr = curr.children[char]
                score += curr.count
            scores.append(score)
            
        return scores
            
        
        
        
        
        
        