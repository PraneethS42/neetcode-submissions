class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # let dp[i] be length of longest inc. ending at i
        # after array computed, need max of dp
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            max_preceding = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_preceding = max(max_preceding, dp[j]+1)
            dp[i] = max_preceding

        return max(dp)
