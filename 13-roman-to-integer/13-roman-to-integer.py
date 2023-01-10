class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        subtract = {
            'I' : {'V', 'X'},
            'X' : {'L' , 'C'},
            'C' : {'D', 'M'}
        }
        
        res = 0
        i = 0
        str_size = len(s)
        
        while i < str_size:
            ch = s[i]
            if ch in subtract and i < len(s) - 1 and \
                s[i + 1] in subtract[ch]:
                res += (value[s[i + 1]] - value[ch])
                i += 2
            else:
                res += value[ch]
                i += 1
                
        return res
    
# First we store each 7 symbols with their respective values in a dictionary.
# Then store those 3 cases where some symbols come before others and their value
# is subtracted from the front one. Then iterate through each char and check if
# the char is in subtract dict and the current index is less than length of the 
# string minus one and the char in front of the current index is in subtract.keys().
# if this condition is satisfied then find the value of the front char and subtract
# the value of the current char from it. Else just find the value of the current char
# add it to result.
