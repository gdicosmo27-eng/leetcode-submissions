class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        for c in s:
            if c == '(' or c == '[' or c == "{":
                stack.append(c)
            elif len(stack) > 0:
                if c == ')':
                    if stack.pop() != '(':
                        return False
                elif c == ']':
                    if stack.pop() != '[':
                        return False
                else:
                    if stack.pop() != '{':
                        return False
            else:
                return False
        return len(stack) == 0