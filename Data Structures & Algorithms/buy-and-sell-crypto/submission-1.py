class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for price in prices[1:]:
            res = max(res, price - min_price)
            min_price = min(min_price, price)
        return res 
