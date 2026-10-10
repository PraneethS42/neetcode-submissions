class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn into set for O(1) lookup
        vals = set(nums)
        mx = 0
        for n in vals:
            if n-1 not in vals: #start of sequence
                curr = 1
                while (n+curr) in vals:
                    curr+=1           
                mx = max(mx, curr)
        return mx
            
