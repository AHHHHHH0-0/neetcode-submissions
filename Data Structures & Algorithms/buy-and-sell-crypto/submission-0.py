class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = float('-inf')
        res = 0
        for price in prices:
            if price < min_price:
                res = max(res, max_price-min_price)
                min_price = price
                max_price = price
            elif price > max_price:
                max_price = price 
        res = max(res, max_price-min_price)
        return res 
