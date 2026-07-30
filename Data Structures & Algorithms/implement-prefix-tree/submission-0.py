class PrefixTree:
    
    class prefixNode:
        def __init__(self):
            self.children = {}
            self.word = False

    def __init__(self):
        self.head = self.prefixNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = self.prefixNode()
                curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        