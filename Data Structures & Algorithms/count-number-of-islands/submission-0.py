class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        n = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                n += Solution.dfs(grid,row,col,visit)
        return n

    def dfs(grid,r,c,visit=set()):
        ROWS, COLS = len(grid), len(grid[0])
        if r <0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or (r,c) in visit or grid[r][c] == "0":
            return 0
        
        visit.add((r,c))
        Solution.dfs(grid,r+1,c,visit)
        Solution.dfs(grid,r,c+1,visit)
        Solution.dfs(grid,r-1,c,visit)
        Solution.dfs(grid,r,c-1,visit)

        return 1