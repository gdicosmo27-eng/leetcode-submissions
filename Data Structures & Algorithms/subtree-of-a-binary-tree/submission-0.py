# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if p and q and p.val == q.val:
            left, right = self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)
            return left and right
        elif not p and not q:
            return True
        else:
            return False
        