class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Strategy - instead of iterating with each element over the remaining ones, just store
        #            remaining quantity: O(n) instead of O(n^2)
        # Key format - Value, then the index
        mapping = {}
        for idx, num in enumerate(nums): # enumerate - first one keeps track of index, second does the value
            if (target-num) in mapping:
                return [mapping[target-num], idx]
            mapping[num] = idx
        

        '''
        if (target-num) in mapping:
                return [mapping[target-num], idx]
            mapping[num] = idx
        '''