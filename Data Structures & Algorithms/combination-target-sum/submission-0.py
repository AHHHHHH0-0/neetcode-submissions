class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def compute(start, t):
            if t < 0:
                return 
            if t == 0:
                res.append(curr.copy())
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                compute(i, t-nums[i])
                curr.pop()
            return
        compute(0, target)
        return res