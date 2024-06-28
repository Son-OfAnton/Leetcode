class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        char_at_even_1, char_at_even_2 = [], []
        char_at_odd_1, char_at_odd_2 = [], []
        
        for i in range(len(s1)):
            if i % 2 == 0:
                char_at_even_1.append(s1[i])
                char_at_even_2.append(s2[i])
            else:
                char_at_odd_1.append(s1[i])
                char_at_odd_2.append(s2[i])
                
        return sorted(char_at_even_1) == sorted(char_at_even_2) and \
                sorted(char_at_odd_1) == sorted(char_at_odd_2)