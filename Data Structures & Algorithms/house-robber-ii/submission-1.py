class Solution:
    def rob_helper(self, nums: List[int]) -> int:
        # Let A[i] be max money using indices {0,..,i}
        A = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                A.append(nums[0])
            elif i == 1:
                A.append(max(nums[0],nums[1]))
            else:
                A.append(max(A[i-1], A[i-2]+nums[i]))  
        return A[-1]

    def rob(self, nums: List[int]) -> int:
        # nums[0] and nums[n-1] can't both be in the result
        # get max 0:n-2 and 1:n-1
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))