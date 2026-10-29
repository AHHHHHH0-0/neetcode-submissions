# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        dq = deque([root, ""])

        vals = []
        while dq:
            node = dq.popleft()
            if node == "":
                ans.append(vals)
                vals = []
                if not dq:
                    return ans
                dq.append("")
                continue
            vals.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return ans

