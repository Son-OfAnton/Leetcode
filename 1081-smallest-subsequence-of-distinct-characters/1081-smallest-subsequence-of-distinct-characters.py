class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index_occured = dict()
        stack = []

        for index, char in enumerate(s):
            last_index_occured[char] = index

        for index, char in enumerate(s):
            if char not in stack:
                while stack and stack[-1] > char and last_index_occured[stack[-1]] > index:
                    stack.pop()
                    
                stack.append(char)

        return "".join(stack)