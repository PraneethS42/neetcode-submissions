class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # Get the product of the first number, then divide by next and multiply by current
        # Get the product of all numbers
        product = 1
        nonzeroprod = 1
        zeroes = 0
        for i in range(0, len(nums)):
            product *= nums[i]
            if nums[i] != 0:
                nonzeroprod *= nums[i]
            else:
                zeroes += 1

        # 3 cases - No zeroes, one zero, more than one zero
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
            for i in range(0,len(nums)):
                ans.append(0)
        return ans

        

        