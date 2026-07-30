# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]): 
        self.ptr = None
        self.stack = []
        
        curr = root
        while curr:
            if curr:
                self.stack.append(curr)
                if curr.left:
                    curr = curr.left
                else:

                    self.ptr = curr.val - 1
                    break
    
    def next(self) -> int:
        curr = self.stack.pop()
        res = curr.val
        curr = curr.right
        while curr:
            if curr:
                self.stack.append(curr)
                if curr.left:
                    curr = curr.left
                else:
                    self.ptr = curr.val - 1
                    return res
        return res
        

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()