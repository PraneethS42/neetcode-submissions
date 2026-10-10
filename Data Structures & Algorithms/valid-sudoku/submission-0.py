class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for val in row:
                if val != "." and val in seen:
                    return False
                seen.add(val)
        
        # Check cols
        for i in range(9): # Per column
            seen = set()
            for j in range(9):
                val = board[j][i]
                if val != "." and val in seen:
                    return False
                seen.add(val)

        # Check squares
        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        val = board[(3*i)+k][(3*j)+l]
                        if val != "." and val in seen:
                            return False
                        seen.add(val)

        return True