class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char in ('[','(','{')):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                elif char == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif char == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()        
        if not len(stack) == 0:
            return False
        return True