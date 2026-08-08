# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        head = ListNode(None, None)
        res = head
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    head.next = curr1
                    head = head.next
                    curr1 = curr1.next
                else:
                    head.next = curr2
                    head = head.next
                    curr2 = curr2.next
            elif curr1:
                head.next = curr1
                head = head.next
                curr1 = curr1.next
            else:
                head.next = curr2
                head = head.next
                curr2 = curr2.next
        return res.next


