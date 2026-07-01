class DSU:
    def __init__(self,size):
        self.parent = list(range(1, size + 1))
        self.rank = [1] * size

    def find(self , i):
        if self.parent[i - 1] == i:
            return i
        self.parent[i - 1] = self.find(self.parent[i - 1])
        return self.parent[i - 1]

    def union(self , i , j):
        irep = self.find(i) - 1
        jrep = self.find(j) - 1

        if irep == jrep : # this is the redundant connection 
            return True 

        if self.rank[irep] > self.rank[jrep]:
            self.parent[jrep] = irep + 1
        elif self.rank[irep] < self.rank[jrep]:
            self.parent[irep] = jrep + 1

        else:
            self.parent[irep] = jrep + 1
            self.rank[jrep] += 1

        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        ans = list(edges[0])
        for u , v in edges:
            flag = dsu.union(u,v)
            if flag:
                ans = [u,v]
        
        return ans
