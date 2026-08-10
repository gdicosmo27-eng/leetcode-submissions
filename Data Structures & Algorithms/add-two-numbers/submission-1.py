# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carried = 0
        while l1 and l2:
            if (l1.val + l2.val + carried) >= 10:
                curr.next = ListNode((l1.val + l2.val + carried) % 10)
                carried = 1
            else:
                curr.next = ListNode((l1.val + l2.val + carried))
                carried = 0
            curr = curr.next
            l1, l2 = l1.next, l2.next
        
        while l1:
            if carried:
                if (l1.val + carried) >= 10:
                    curr.next = ListNode((l1.val + carried) % 10)
                    carried = 1
                else:
                    curr.next = ListNode((l1.val + carried))
                    carried = 0
            else:
                curr.next = ListNode(l1.val)
            curr = curr.next
            l1 = l1.next

        while l2:
            if carried:
                if (l2.val + carried) >= 10:
                    curr.next = ListNode((l2.val + carried) % 10)
                    carried = 1
                else:
                    curr.next = ListNode((l2.val + carried))
                    carried = 0
            else:
                curr.next = ListNode(l2.val)
            curr = curr.next
            l2 = l2.next

        if carried:
            curr.next = ListNode(carried)

        return dummy.next
            