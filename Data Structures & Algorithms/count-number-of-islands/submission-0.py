class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS , COLS  = len(grid) , len(grid[0])
        def dfs(r,c,visited,directions):
            visited.add((r,c))
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if (nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or 
                    grid[nr][nc] == '0' or (nr,nc) in visited):
                    continue 
                dfs(nr,nc, visited , directions)

        ans = 0
        visited = set()
        directions = [[0,1] , [1,0] ,[0,-1] , [-1,0]]
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c,visited , directions)
                    ans += 1

        return ans

        

