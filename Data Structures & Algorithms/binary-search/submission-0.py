class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l <= r: # Needed instead of l < r to allow another iteration in case element resides at l or r
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1 # Adding 1 prevents getting stuck - plus mid isn't the right value anyways
            else:
                r = mid-1
        return -1