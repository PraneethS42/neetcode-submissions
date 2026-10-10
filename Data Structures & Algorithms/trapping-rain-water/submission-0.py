class Solution:
    def trap(self, height: List[int]) -> int:
        ttl = 0
        # Find a left max, once a right max passes it, can't trap more
        # Iterate till right reaches the end
        # l,r = 0,1
        # maxLeft, maxRight = 0,0

        # while r < len(height):
        #     # Hit a peak
        #     if height[l] < height[r]:

        # Brute force solution first
        for i in range(1, len(height)-1):
            # height = min(height[l], height[r]) - height[i]
            # need to finx max for each part
            # omit first and last 
            leftMax, rightMax = 0, 0
            for k in range(i, -1, -1):
                leftMax = max(height[k], leftMax)
            for k in range(i, len(height)):
                rightMax = max(height[k], rightMax)
            ttl += max(min(leftMax, rightMax) - height[i], 0)
        
        return ttl
        