class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Height = min(left and right) * (r-l) <- distance
        mx = 0
        lp, rp = 0, len(heights)-1

        while lp < rp:
            height = min(heights[lp], heights[rp]) * (rp-lp)
            mx = max(mx, height)

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        return mx
