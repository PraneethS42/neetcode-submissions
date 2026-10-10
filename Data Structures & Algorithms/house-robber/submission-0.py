class Solution:
    def rob(self, nums: List[int]) -> int:
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