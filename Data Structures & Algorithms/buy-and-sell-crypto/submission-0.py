class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want to store lowest
        # once we get a lower value than the left we can replace it
        highest = 0
        l, r = 0,0
        while r < len(prices):
            if prices[r] < prices[l]: # less than amount
                l = r # move to right amount
            highest = max(highest, prices[r]-prices[l])
            r += 1
        return highest
        