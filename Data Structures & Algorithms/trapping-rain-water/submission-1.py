class Solution:
    def trap(self, height: List[int]) -> int:
        ttl = 0
        leftMaxes, rightMaxes = [0]*len(height), [0]*len(height)
        # create arrays for prefix/postfix - should be done in O(n)
        for i in range(1, len(height)):
            leftMaxes[i] = max(height[i-1], leftMaxes[i-1])
        for i in range(len(height)-2,-1,-1):
            rightMaxes[i] = max(height[i+1], rightMaxes[i+1])
        for i in range(0, len(height)):
            ttl += max(min(leftMaxes[i], rightMaxes[i])-height[i],0)
        return ttl


        