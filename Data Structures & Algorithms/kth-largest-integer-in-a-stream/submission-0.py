class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # store the k largest elements in our min heap -> kth largest is the smallest, so at root
        self.amnt = k
        self.heap = nums  # min heap
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        # heap insert
        # look for kth largest element
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.amnt:
            heapq.heappop(self.heap)
        return self.heap[0]
