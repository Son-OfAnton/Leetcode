class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size  = len(s)
        arr = [0] * len(s)
        
        for shift in shifts:
            if shift[2] == 0:
                arr[shift[0]] -= 1
                
                if shift[1] + 1 != size:
                    arr[shift[1] + 1] += 1
            else:
                arr[shift[0]] += 1
                
                if shift[1] + 1 != size:
                    arr[shift[1] + 1] -= 1
        
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
                
        s = list(s)
        
        for i in range(len(arr)):
            s[i] = chr((((ord(s[i]) + arr[i]) - 97) % 26) + 97)
            
        return "".join(s)
            
        
# First we need a list of size len(s) which records the shift for each letter.
# Then for every shift query's first index we will record the true shift(-1 for 0 and +1 for 1).
# For the second index we record the opposite shift (+1 for 0 and -1 for 1). 
# Then we will apply prefic sum on the record list. This creates an list which 
# applies true shift for the wanted range and cancels the changes made on chars 
# outside the range.
# Finally we will convert the string into char list and update each of them.