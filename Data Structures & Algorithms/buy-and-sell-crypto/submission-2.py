class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l,r=0,1
        maxPrice = 0

        while r < len(nums):
            if nums[l] < nums[r]:
                maxPrice = max(maxPrice, nums[r]-nums[l])
            else:
                l = r
            r += 1 
        return maxPrice