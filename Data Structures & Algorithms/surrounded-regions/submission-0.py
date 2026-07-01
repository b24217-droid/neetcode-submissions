class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS , COLS = len(board) , len(board[0])
        visited = set()
        directions = [(1,0) , (-1,0) ,(0,1) ,(0,-1)]

        def dfs(r,c):
            stack = []
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r + dr , c + dc
                if (nr < 0 or nc < 0 or 
                    nr >= ROWS or nc >= COLS or
                    board[nr][nc] == "X" or (nr,nc) in visited):
                    continue

                stack.append((nr,nc))
        
            while stack:
                r1,c1 = stack.pop()
                dfs(r1,c1)


        # top boundary
        for c in range(COLS):
            if board[0][c] == "O" and (0,c) not in visited:
                dfs(0,c)
            if board[ROWS - 1][c] == "O" and (ROWS - 1 , c) not in visited:
                dfs(ROWS - 1 , c)

        # left and right
        for r in range(ROWS):
            if board[r][0] == "O" and (r,0) not in visited:
                dfs(r,0)
            if board[r][COLS - 1] == "O" and (r , COLS - 1) not in visited:
                dfs(r , COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    if (r,c) not in visited:
                        board[r][c] = "X"
    
            