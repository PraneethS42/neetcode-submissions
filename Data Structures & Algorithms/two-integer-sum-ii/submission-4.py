class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # List comes sorted
        # Since O(1) additional space, can't store hash map
        # Go two ptrs and converge
        lp,rp=0,len(numbers)-1
        while lp < rp:
            if (numbers[lp]+numbers[rp]) == target:
                return [lp+1,rp+1]
            elif (numbers[lp]+numbers[rp]) < target:
                lp+=1
            else:
                rp-=1