class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        num = 0
        operator = '+'
        signs = {'+', '-', '*', '/'}

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in signs and char != ' ' or i == n - 1:     # i==n-1 is needed for cases as ['42']
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                operator = char
                
        return sum(stack)

