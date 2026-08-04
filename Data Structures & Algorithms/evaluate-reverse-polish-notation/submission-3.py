import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a/b) 
        }
        
        stack = []
        for t in tokens:
            if t in ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(ops[t](arg1, arg2))
            else:
                stack.append(int(t))

        return stack.pop() 