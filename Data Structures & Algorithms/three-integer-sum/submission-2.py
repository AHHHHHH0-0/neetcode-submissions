from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        seen = set(tuple())
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        for i in range(len(nums)):
            d[nums[i]] -= 1
            for j in range(i+1, len(nums)):
                d[nums[j]] -= 1
                third = -(nums[i] + nums[j])
                if d[third] > 0:
                    l = sorted([nums[i], nums[j], third])
                    if tuple(l) not in seen:
                        solution.append(l)
                        seen.add(tuple(l))
                d[nums[j]] += 1
            d[nums[i]] += 1
        return solution      

