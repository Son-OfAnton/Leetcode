class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation_set = {"+", "-", "*", "/"}
        
        for item in tokens:            
            if item not in operation_set:            
                stack.append(int(item))
            else:       
                num2 = stack.pop()
                num1 = stack.pop()
                
                if item == "+":
                    stack.append(num1 + num2)
                elif item == "-":
                    stack.append(num1 - num2)
                elif item == "*":
                    stack.append(num1 * num2)
                elif item == "/":
                    stack.append(int(num1 / num2))
        
        return stack[0]