class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Cut the list in half
        prev.next = None

        reverse = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = temp
        
        # Merge the two halves
        dummy = ListNode(0)
        curr = dummy
        p1, p2 = head, reverse
        while p1 or p2:
            if p1:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            if p2:
                curr.next = p2
                p2 = p2.next
                curr = curr.next