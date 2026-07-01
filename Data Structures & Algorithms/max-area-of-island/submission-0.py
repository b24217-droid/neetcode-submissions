class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c,visited , directions,area):
            if grid[r][c] == 0:
                return 0

            visited.add((r,c))
            for dr , dc in directions:
                nr , nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or
                    (nr , nc) in visited):
                    continue
                if grid[nr][nc] == 1:
                    area = dfs(nr , nc,visited , directions , area + 1)

            return area

        ROWS , COLS = len(grid) , len(grid[0])
        max_area = 0
        visited = set()
        directions = [(0,1) , (1, 0),(-1,0),(0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c,visited , directions,1)
                    max_area = max(max_area , area)

        return max_area
        
