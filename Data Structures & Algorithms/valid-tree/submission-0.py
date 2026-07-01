from collections import defaultdict
class DSU:
    def __init__(self, size: int):
        # Each node is initially its own parent
        self.parent = list(range(size))
        # Rank is used to keep the tree flat during union
        self.rank = [1] * size

    def find(self, i: int) -> int:
        # Path compression optimization
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        
        # If roots are the same, a cycle is detected!
        if root_i == root_j:
            return False
            
        # Union by rank optimization
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = self.construct(edges)
        if self.has_Cycle(n,edges):
            return False
        if not self.connected(n,adj):
            return False
        
        return True

    def connected(self , n , adj):
        q= deque([0])
        visited = {0}

        while q:
            node = q.popleft()
            for nbr in adj[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        
        return len(visited) == n

    def construct(self, edges): # to make adj list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

    def has_Cycle(self,n: int, edges: list[list[int]]) -> bool:
        dsu = DSU(n)
        
        for u, v in edges:
            if not dsu.union(u, v):
                return True
                
        return False

