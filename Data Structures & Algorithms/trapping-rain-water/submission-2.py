class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ttl = 0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax <= rightMax:
                l += 1
                ttl += max(leftMax-height[l],0)
                leftMax = max(height[l], leftMax)
            else: # leftMax > rightMax
                r -= 1
                ttl += max(rightMax-height[r],0)
                rightMax = max(height[r], rightMax)
        return ttl


        

        