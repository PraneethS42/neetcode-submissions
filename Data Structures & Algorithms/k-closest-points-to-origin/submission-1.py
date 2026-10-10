class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:   # O(n)
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap) # O(n)
        res = []
        while k > 0:  # O(klogn)
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
