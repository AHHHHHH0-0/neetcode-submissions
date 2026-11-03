class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running = 0
        res = -float("INF")
        for num in nums:
            running += num
            res = max(res, running)
            if running < 0:
                running = 0
        return res