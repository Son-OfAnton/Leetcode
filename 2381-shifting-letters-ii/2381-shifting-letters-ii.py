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
        print(arr)
        
        for i in range(len(arr)):
            s[i] = chr((((ord(s[i]) + arr[i]) - 97) % 26) + 97)
            
        return "".join(s)
            