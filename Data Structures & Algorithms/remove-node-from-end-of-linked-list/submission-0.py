# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        res = head 
        while head:
            count += 1
            head = head.next
        if n == count:
            return res.next
        head = res.next
        prev = res
        while head:
            if n == count-1:
                prev.next = head.next
                return res
            prev = head
            head = head.next
            count -= 1
