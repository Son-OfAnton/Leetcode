class Solution(object):
    def countVowels(self, word):
        n = len(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        
        for i in range(n):
            if word[i] in vowels: 
                res += (n - i) * (i + 1)
        
        return res