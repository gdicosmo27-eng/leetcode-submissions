# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        cur = head.next
        prev = head
        prev.next = None
        while cur:
            temp = prev
            prev = cur
            cur = cur.next
            prev.next = temp
        return prev


