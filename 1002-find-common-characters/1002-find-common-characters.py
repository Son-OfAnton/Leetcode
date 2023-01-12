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

        for index, freq in enumerate(common):
            if freq:
                for i in range(freq):
                    common_chars.append(chr(offset + index))
                
        return common_chars
    
    
# We use a common list to count the chars by mapping their ascii value to common's
# index by subtracting ascii value of 'a' from their ascii value. Then we will
# count the char frequency of the first word. Since common letters are necesarily
# found in the first word, we will do the same for the rest of the words and take 
# the min freq. Finaly we will append the real chars by reverse mapping the indexes
# to ascii values and undoing the offset.
        
        
        