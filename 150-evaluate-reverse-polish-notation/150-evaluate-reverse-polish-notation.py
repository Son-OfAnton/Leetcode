class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '/', '*'}

        for char in tokens:
            if char not in operands:
                stack.append(char)
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()

                if char == '+':
                    stack.append(int(num_1) + int(num_2))
                elif char == '-':
                    stack.append(int(num_1) - int(num_2))
                elif char == '*':
                    stack.append(int(num_1) * int(num_2))
                elif char == '/':
                    stack.append(int(num_1) / int(num_2))

        return int(stack.pop())

    