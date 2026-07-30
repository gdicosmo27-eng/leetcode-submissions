# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPath(root, targetSum):
            if not root:
                return False
            
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                return True
            if root.left:
                if hasPath(root.left, targetSum):
                    return True
            if root.right:
                if hasPath(root.right, targetSum):
                    return True
            else:
                targetSum += root.val
                return False
        
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            else:
                return False
        if hasPath(root.left, targetSum):
            return True
        elif hasPath(root.right, targetSum):
            return True
        return False

