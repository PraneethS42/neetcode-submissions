class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Need O(n) space and time
        # Each index n is the collection of numbers that appears n times 
        #      thats why it must be blank
        freq = [[] for i in range(0, len(nums) + 1)]
        c = {}
        for num in nums:
            c[num] = 1 + c.get(num, 0)  # Basically returns 0 if not already a key, or else add to existing
        for key, value in c.items(): # .items() is ESSENTIAL
            freq[value].append(key)

        ans = []
        for i in range(len(freq) - 1, 0, -1): # Iterate backward
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

