class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '/', '*'}

        for char in tokens:
            if char not in operands:
                stack.append(char)
            else:
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())

                if char == '+':
                    stack.append(num_1 + num_2)
                elif char == '-':
                    stack.append(num_1 - num_2)
                elif char == '*':
                    stack.append(num_1 * num_2)
                elif char == '/':
                    stack.append(num_1 / num_2)

        return int(stack.pop())

    