class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitted = path.split('/')
        
        for directory in splitted:
            if directory == "" or directory == ".": 
                continue
            elif directory == "..": 
                if stack: 
                    stack.pop()
            else:
                stack.append(directory)
        
        return f"/{'/'.join(stack)}"