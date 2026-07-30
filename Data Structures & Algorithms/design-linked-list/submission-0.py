class MyLinkedList:

    class Node():
        def __init__(self, val = None, nxt = None, prev = None):
            self.val = val
            self.nxt = nxt
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        else:
            cur = self.head
            for i in range(index):
                if cur.nxt:
                    cur = cur.nxt
                else:
                    return -1
            return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.nxt = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = self.Node(val)
        if not self.tail:
            self.tail = newNode
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.nxt = newNode
            newNode.nxt = None
            self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            newNode = self.Node(val)
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode = self.Node(val)
            self.head.prev = newNode
            newNode.nxt = self.head
            self.head = newNode
        else:
            cur = self.head
            for i in range(index - 1):
                if not cur.nxt:
                    return
                else:
                    cur = cur.nxt
            if not cur.nxt:
                newNode = self.Node(val)
                self.tail.nxt = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                newNode = self.Node(val)
                temp = cur.nxt
                temp.prev = newNode
                newNode.nxt = temp
                newNode.prev = cur
                cur.nxt = newNode


    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        elif index == 0:
            temp = self.head.nxt
            temp.prev = None
            self.head = temp
        else:
            cur = self.head
            for i in range(index):
                if not cur.nxt:
                    return
                else:
                    cur = cur.nxt
            if not cur.nxt:
                self.tail = cur.prev
                self.tail.nxt = None
            else:
                temp = cur.nxt
                cur.prev.nxt = temp
                temp.prev = cur.prev
            



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)