class Solution:    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n = len(words)
        
        for index, query in enumerate(queries):
            queries[index] = query.count(min(query))
        
        for index, word in enumerate(words):
            words[index] = word.count(min(word))
        
        words.sort()
        res = []
        
        for query in queries:
            res.append(n - bisect_right(words, query))
            
        return res
            