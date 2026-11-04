class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = dict()
        def climb(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            next_cost = cost[i] + min(climb(i+1), climb(i+2))
            cache[i] = next_cost
            return next_cost
        return min(climb(0), climb(1))