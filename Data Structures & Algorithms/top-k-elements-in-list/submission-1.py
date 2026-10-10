class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Populate dictionary in num - quantity format
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        keys = list(freq.keys())
        values = list(freq.values())
        values.sort()

        # Extract the max value each time and append the key if the value matches, then remove
        ans = []
        for i in range(k):
            maxval = values.pop()
            for j in keys:
                if freq[j] == maxval:
                    ans.append(j)
                    keys.remove(j)
        return ans



