class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Let A[i] be min. cost to get to index i
        A = [1] * len(cost)
        A[0] = cost[0]
        A[1] = cost[1]
        for i in range(2, len(cost)):
            A[i] = cost[i] + min(A[i-1], A[i-2])

        return min(A[-1], A[-2])