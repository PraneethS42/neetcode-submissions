class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            # While greater than top, keep going
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = index - stackInd
            # Add after, so we can pop from it before without this being in the way
            stack.append((temp, index))
        return res