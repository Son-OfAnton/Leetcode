class TrieNode:
    
    def __init__(self):
        
        self.is_end = False
        self.children = dict()
        

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True


    def find_end_count(self, word: str) -> bool:
        curr = self.root
        end_count = 0
        for char in word:
            curr = curr.children[char]
            if curr.is_end:
                end_count += 1
            else:
                break

        return end_count

        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        dictionary = Trie()
        for word in words:
            dictionary.insert(word)

        word_end_count = dict()
        max_end_count = 0
        
        for word in words:
            end_count = dictionary.find_end_count(word)
            if end_count >= max_end_count:
                max_end_count = end_count
                longest_word_built_by_others = word
            word_end_count[word] = end_count

        if max_end_count == 0:
            return ''
        for word, end_count in word_end_count.items():
            if end_count == max_end_count:
                longest_word_built_by_others = min(longest_word_built_by_others, 
                                                    word)

        return longest_word_built_by_others