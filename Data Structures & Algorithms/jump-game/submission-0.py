class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = set()
        stack = [0]
        n = len(nums)
        while stack:
            idx = stack.pop()
            if idx >= n-1:
                return True
            if nums[idx] == 0:
                continue
            for i in range(1, nums[idx]+1):
                if idx+i not in seen:
                    seen.add(idx+i)
                    stack.append(idx+i)
        return False