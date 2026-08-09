class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        start = l
        l = 0
        r = len(nums)-1

        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r = start - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1