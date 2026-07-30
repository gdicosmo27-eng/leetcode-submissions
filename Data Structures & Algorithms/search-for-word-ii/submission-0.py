class Solution:
    class Trie:
        class PrefixNode:
            def __init__(self):
                self.children = {}
                self.word = False

        def __init__(self):
            self.head = self.PrefixNode()
        
        def insert(self, word):
            curr = self.head
            for c in word:
                if c not in curr.children:
                    curr.children[c] = self.PrefixNode()
                curr = curr.children[c]
            curr.word = word
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return
            if board[r][c] not in node.children:
                return
            
            node = node.children[board[r][c]]

            if node.word:
                res.append(node.word)
                node.word = False

            temp = board[r][c]
            board[r][c] = '#'

            dfs(node, r - 1, c)
            dfs(node, r, c - 1)
            dfs(node, r + 1, c)
            dfs(node, r, c + 1)

            board[r][c] = temp
        
        ROWS, COLS = len(board), len(board[0])
    
        # build trie
        trie = self.Trie()
        for word in words:
            trie.insert(word)
    
        res = []
    
        for r in range(ROWS):
            for c in range(COLS):
                dfs(trie.head, r, c)
    
        return res
        