class MyLinkedList:

    class Node():
        
        def __init__(self, val = None, next = None):
            self.val = val
            self.next = next

    def __init__(self):
        self.dummy = self.Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            cur = self.dummy.next
            for i in range(index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = self.Node(val, cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

                




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)