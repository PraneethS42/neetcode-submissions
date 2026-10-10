class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two sum but sorted
        fp, bp = 0, len(numbers)-1
        while fp < bp:
            if numbers[fp] + numbers[bp] == target:
                return [fp+1, bp+1]
            if numbers[fp] + numbers[bp] > target:
                bp-=1
            else:
                fp+=1