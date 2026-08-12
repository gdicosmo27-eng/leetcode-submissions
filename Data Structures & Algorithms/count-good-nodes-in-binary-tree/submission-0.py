# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        res = 0
        
        if root:
            queue.append((root, root.val))
            res += 1
        
        while queue:
            for i in range(len(queue)):
                curr, maxInPath = queue.popleft()
                if curr.left:
                    if curr.left.val >= maxInPath:
                        res += 1
                        queue.append((curr.left, curr.left.val))
                    else:
                        queue.append((curr.left, maxInPath))
                if curr.right:
                    if curr.right.val >= maxInPath:
                        res += 1
                        queue.append((curr.right, curr.right.val))
                    else:
                        queue.append((curr.right, maxInPath))
        return res
