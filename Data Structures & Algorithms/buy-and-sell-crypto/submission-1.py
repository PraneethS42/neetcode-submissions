class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxProf = 0
        minFar = 101

        for i in range(len(nums)):
            if nums[i] < minFar: # Now we have min at every index
                minFar = nums[i]

            if (nums[i]-minFar) > maxProf:
                maxProf = nums[i]-minFar
        
        return maxProf