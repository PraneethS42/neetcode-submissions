class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The max frequency is the length of the list, so maybe create an array of that length
        buckets = [[] for i in range(len(nums)+1)]
        freq = {}

        # Creating the frequency map
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for number, count in freq.items(): # Tip to go through key and item
            buckets[count] += [number]
        
        # Now iterate backwards
        output = []
        p = len(nums)-1

        while k > 0:
            if not buckets[p]:
                p -= 1
            else:
                output.append(buckets[p].pop())
                k -= 1
        return output

            