class Solution:
    def decodeString(self, s: str) -> str:
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