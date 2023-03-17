class Solution:
    def __init__(self):
        self.s = None
        
    def decoder(self, index):
        """
        Recursive solution
        """
        decoded = ""
        mult = 0

        while index < len(self.s):
            char = self.s[index]

            if char.isdigit():
                mult = mult * 10 + int(char)
            elif char == '[':
                inner_string, last_index = self.decoder(index + 1)
                decoded += mult * inner_string
                index = last_index
                mult = 0
            elif char == ']':
                return decoded, index
            else:
                decoded += char
            
            index += 1

        return decoded, index

    def decodeString(self, s: str) -> str:
        self.s = s
        
        return self.decoder(0)[0]

    
    
    
"""
Iterative solution

stack = []

for char in s:
    if char != ']':
        stack.append(char)
    else:
        inner = ""
        while stack[-1] != '[':
            inner = stack.pop() + inner
        stack.pop()

        num = ""
        while stack and stack[-1].isdigit():
            num = stack.pop() + num
        stack.append(int(num) * inner)

return "".join(stack)

"""