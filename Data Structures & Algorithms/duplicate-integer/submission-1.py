class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for item in nums:
            if item in seen:
                return True
            seen[item] = 1
        return False
         
        '''
        could also replace dict = {} with 
        ''' 