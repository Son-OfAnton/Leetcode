class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [float("inf")] * 26
        offset = ord('a')
        
        for word in words:
            curr_count = [0] * 26
            
            for char in word:
                curr_count[ord(char) - offset] += 1
            
            for index in range(26):
                common[index] = min(common[index], curr_count[index])
        
        common_chars = []
        print(common)

        for index, freq in enumerate(common):
            if freq:
                for i in range(freq):
                    common_chars.append(chr(offset + index))
                
        return common_chars
        
        
        