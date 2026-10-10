class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check 9 rows, 9 cols and 9 boxes
        n = len(board)
        rows = [set() for y in range(n)]
        cols = [set() for x in range(n)]
        squares = [set() for x in range(n)]

        for y in range(n):
            for x in range(n):
                val = board[y][x]

                if val == '.':
                    continue

                sq =(y // 3) * 3 + x // 3
                if val in rows[y] or val in cols[x] or val in squares[sq]:
                    return False
                else:
                    rows[y].add(val)
                    cols[x].add(val)
                    squares[sq].add(val)
        
        return True