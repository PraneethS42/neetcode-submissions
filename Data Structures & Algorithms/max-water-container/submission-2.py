class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calc of volume -> min(l,r)*(r-l)
        # always limited by the smallest value, move that one instead of the larger
        # two pointer approach
        l,r = 0, len(heights)-1
        volume = 0
        while l < r:
            volume = max(volume, (r-l)*min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return volume

