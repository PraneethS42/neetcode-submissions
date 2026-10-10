class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(x,y):
            if ((x,y) in visited) or x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == "0":
                return
            visited.add((x,y))
            # Branch in directions
            for direc in directions:
                dfs(x+direc[0], y+direc[1])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
        
        return islands