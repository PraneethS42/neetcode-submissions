class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # First iteration - Store in result the prefix product of the elements before it
        prefix = 1
        for i in range(len(nums)):
            # Store the result to the existing prefix sum, then multiply the product of that num
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        

        