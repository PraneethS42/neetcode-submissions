class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Value of container -> (r-l)*min(l,r)
        # If move the larger value inwards, then (r-l) gets smaller while min(l,r) stays the same or lower
        # Therefore, move the smaller value inwards
        hmax = 0 
        lp, bp = 0, len(heights)-1
        while lp < bp:
            hmax = max(hmax, (bp-lp)*min(heights[lp],heights[bp]))
            if heights[bp] < heights[lp]:
                bp-=1
            else:
                lp+=1
        return hmax


        
