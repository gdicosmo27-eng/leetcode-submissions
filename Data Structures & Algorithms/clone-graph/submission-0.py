"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        cloned = {}
        
        def clone(node):
            if not node or node in cloned:
                return
            newNode = Node(node.val, [])
            cloned[node] = newNode
            
            for neighbor in node.neighbors:
                clone(neighbor)
                newNode.neighbors.append(cloned[neighbor])
        
        clone(node)
        return cloned[node]
            