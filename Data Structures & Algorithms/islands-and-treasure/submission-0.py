class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS , COLS = len(grid) , len(grid[0])
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c)) # r,c, dist

        if not q:
            return

        directions = [(0,1) , (1, 0 ) , (0,-1) , (-1, 0)]
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r,c = q.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == -1):
                        continue
                    
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))

                        
                    
