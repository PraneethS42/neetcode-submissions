class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        lp, rp = 0, h-1
        # For any index, height at that array is max height to the left and right
        prefix, postfix = [0]*h, [0]*h
        prefix[0] = height[0]
        postfix[h-1] = height[h-1]

        for i in range(1,h):
            prefix[i] = max(prefix[i-1], height[i])
        for i in range(h-2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i])
        # Now that these are generated, calc height
        res = 0
        for i in range(h):
            res += min(prefix[i], postfix[i]) - height[i]
        return res
        

        