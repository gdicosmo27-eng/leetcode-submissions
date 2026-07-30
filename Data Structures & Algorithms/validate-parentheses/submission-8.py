class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) > 0:
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        return len(stack) == 0
        
