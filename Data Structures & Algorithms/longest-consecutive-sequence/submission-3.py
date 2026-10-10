class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_no = 0
        running = 0
        # Only consider a number if it might start a sequence
        for num in s:
            if num-1 not in s:
                # Check until sum stalls
                x = num
                while x in s:
                    x += 1
                    running += 1
                max_no = max(max_no,running)
                running = 0
        return max_no
        