# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if p and q and p.val == q.val:
                left, right = dfs(p.left, q.left), dfs(p.right, q.right)
                return left and right
            elif not p and not q:
                return True
            else:
                return False

        return dfs(p, q)