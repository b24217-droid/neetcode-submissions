class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = self.construct(n , edges)

        def bfs(i,visited):
            q = deque([i])
            visited.add(i)
            while q:
                node = q.popleft()
                for nbr in adj[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
        
        components = 0
        for i in range(n):
            if i not in visited:
                bfs(i,visited)
                components += 1
        
        
        return components



    def construct(self , n ,edges):
        adj = collections.defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
                
        return adj