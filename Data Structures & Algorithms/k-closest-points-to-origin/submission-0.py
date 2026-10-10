class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance = euclidian formula
        # same strat? once above k we can discard
        # store current max in heap
        max_heap = []
        for pt in points:
            distance = (pt[0])**2 + (pt[1])**2
            heapq.heappush(max_heap, (-distance,pt))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        pts = []
        for item in max_heap:
            pts.append(item[1])
        return pts
