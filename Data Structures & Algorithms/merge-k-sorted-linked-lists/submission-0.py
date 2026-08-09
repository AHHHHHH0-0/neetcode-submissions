# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        master_list = []
        for node in lists:
            while node:
                master_list.append(node.val)
                node = node.next
        master_list.sort(reverse=True)
        ans_node = None
        for value in master_list:
            ans_node = ListNode(value, ans_node)
        return ans_node