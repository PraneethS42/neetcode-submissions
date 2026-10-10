class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Fix first variable 
        ans = []
        for i in range (len(nums)):
            target = 0 - nums[i] 
            stored = set()
            for idx, num in enumerate(nums[i+1:]):
                if (target-num) in stored:
                    arr = [nums[i], target-num, num]
                    arr.sort()
                    if arr not in ans:
                        ans.append(arr)
                else:
                    stored.add(num)
        
        return ans

        