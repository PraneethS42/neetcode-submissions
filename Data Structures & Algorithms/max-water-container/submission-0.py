class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The volume is equal to the height x width
        # The height - min(left bar, right bar)
        # The width - (index2-index1), number of elements consisting of both
        maxval = 0
        l, r = 0, len(heights) - 1
        while l < r:
            vol = min(heights[l], heights[r])*(r-l)
            if vol > maxval:
                maxval = vol
            # Now we need to move the pointers
            # We should move the lower column, because no matter the other column the max 
            #   that the height can be is that height, while the width constricts
            if heights[l] <= heights[r]: # Left is smaller or equal, both work
                l += 1
            elif heights[l] > heights[r]: # Right is smaller
                r -= 1
        return maxval

