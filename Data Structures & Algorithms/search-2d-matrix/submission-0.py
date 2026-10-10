class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search on m*n elements
        m,n = len(matrix), len(matrix[0])
        left,right = 0, m*n-1
        while left <= right:
            mid = left + (right-left)//2
            r = mid//n  
            c = mid%n

            if (matrix[r][c] == target):
                return True
            if (matrix[r][c] < target):
                left = mid+1
            else:
                right = mid-1
           
        
        return False