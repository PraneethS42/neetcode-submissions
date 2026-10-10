class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Get the product of all numbers
        product = 1
        nonzeroprod = 1
        zeroes = 0
        for num in nums:
            product *= num
            if num != 0:
                nonzeroprod *= num
            else:
                zeroes += 1

        # 3 cases - No zeroes, one zero, more than one zero
        ans = []
        if zeroes == 0:
            for i in range(0,len(nums)):
                ans.append(int(product//nums[i]))
        if zeroes == 1:
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    ans.append(nonzeroprod)
                else:
                    ans.append(0)
        if zeroes > 1:
            return [0] * len(nums)
        return ans

        

        