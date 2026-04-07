# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1

        m = count - n
        if m == 0:
            return head.next
        
        curr = head
        for i in range(m):
            if i == m - 1:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head