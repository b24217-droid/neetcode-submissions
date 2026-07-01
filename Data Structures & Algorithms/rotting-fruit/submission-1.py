from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # you do multi source bfs
        # you take all the rotten and calculate the time ?
        ROWS  ,COLS = len(grid) , len(grid[0])
        if not grid:
            return 0

        time_taken = -1
        oranges_count = 0
        q = deque() # take r,c
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    oranges_count += 1

        if oranges_count == 0 : return 0

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r,c = q.popleft()
                for dr ,dc in directions:
                    nr , nc = r + dr , c + dc
                    if (nr < 0 or nc < 0 or 
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != 1 ):
                        continue
                
                    q.append((nr,nc))
                    grid[nr][nc] = 2
                    oranges_count -=1
            time_taken += 1


        return time_taken if oranges_count == 0 else -1

                

            
            