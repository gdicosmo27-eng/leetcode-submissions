# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            return max(depth(node.right), depth(node.left)) + 1

        if root.left:
            left = depth(root.left) 
        else:
            left = 0
        if root.right:
            right = depth(root.right)
        else:
            right = 0
        
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
                
                
                
            
            
