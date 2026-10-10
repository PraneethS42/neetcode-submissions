class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # O[i] = nums[1,2,..,i-1] * nums[i+1,len]
       #      = pref
       # One array (prefix) stores product of all items to left, other has all to right
       # Find edge cases and off by 1s later
       prefix, postfix = [1]*len(nums), [1]*len(nums)

       for i in range(1, len(nums)): #prefix -> [1,1,2,8]
            prefix[i] = nums[i-1] * prefix[i-1]

       for i in range(len(nums)-2,-1,-1): #postfix -> [48,24,6,1]
            postfix[i] = nums[i+1] * postfix[i+1] 

       res = []
       for i in range(len(prefix)):
            res.append(prefix[i]*postfix[i])
       return res


        