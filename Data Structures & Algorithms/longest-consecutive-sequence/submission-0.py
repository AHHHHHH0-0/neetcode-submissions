class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        run = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                l = 1
                while num + 1 in num_set:
                    l += 1
                    num += 1
                run = max(l, run)
        return run

