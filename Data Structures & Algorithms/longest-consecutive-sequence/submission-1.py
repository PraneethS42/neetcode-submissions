class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        running_sum = 1
        found_max = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                running_sum += 1
            else:
                if running_sum > found_max:
                    found_max = running_sum
                running_sum = 1
        return max(running_sum,found_max)

        