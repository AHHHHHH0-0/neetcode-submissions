class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in checked:
                return [checked[target - nums[i]], i]
            checked[nums[i]] = i
        return []