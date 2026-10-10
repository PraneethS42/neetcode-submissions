class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {} # number, then index
        for i in range(len(nums)):
            if (target-nums[i]) in rem:
                return [rem[target-nums[i]], i]
            rem[nums[i]] = i
