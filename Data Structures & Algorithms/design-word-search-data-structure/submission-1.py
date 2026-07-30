class WordDictionary:
    class PrefixNode:
        def __init__(self):
            self.children = {}
            self.word = False

    def __init__(self):
        self.head = self.PrefixNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.PrefixNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.word
            
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)
        
        return dfs(self.head, 0)
                



    
        
