class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq = {}
        for n in nums: # O(n)
            freq[n] = 1 + freq.get(n,0)
        # Now have a map of every element and their freq
        for elem in freq: # O(n)
            num = freq[elem]
            buckets[num].append(elem)

        # Now return the k most
        res = []
        p = len(nums)-1
        while k > 0: # Invariant says this will run out first
            if not buckets[p]:
                p-=1
            else:
                res.append(buckets[p].pop()) # Remove one, don't move the index down
                k-=1
        return res
