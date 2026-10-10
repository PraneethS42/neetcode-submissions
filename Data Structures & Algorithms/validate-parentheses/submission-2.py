class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in mp:
                if len(stack) == 0:
                    return False
                if mp[char] != stack[-1]:
                    return False
                else: 
                    stack.pop()
            else:
                stack.append(char)       
        return len(stack) == 0