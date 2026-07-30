class BrowserHistory:

    class Node:

        def __init__(self, url = None, prev = None, next = None):
            self.url = url
            self.prev = prev
            self.next = next

    def __init__(self, homepage: str):
        self.home = self.Node(homepage)
        self.end = self.Node()
        self.home.next = self.end
        self.end.prev = self.home
        self.cur = self.home

    def visit(self, url: str) -> None:
        newNode = self.Node(url)
        self.cur.next = newNode
        newNode.prev = self.cur
        newNode.next = self.end
        self.end.prev = newNode
        self.cur = newNode

    def back(self, steps: int) -> str:
        while self.cur != self.home and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur != self.end and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        if self.cur == self.end:
            self.cur = self.cur.prev
            return self.cur.url
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)