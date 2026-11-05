class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            if heaviest == stones[0]:
                heapq.heappop_max(stones)
            else:
                _ = heapq.heapreplace_max(stones, heaviest-stones[0])

        if stones:
            return stones[0]
        else: 
            return 0 