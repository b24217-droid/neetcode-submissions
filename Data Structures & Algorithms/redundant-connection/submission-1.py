class DSU:
    def __init__(self,size):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self , i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self , i , j):
        irep = self.find(i) 
        jrep = self.find(j) 

        if irep == jrep : # this is the redundant connection 
            return True 

        if self.rank[irep] > self.rank[jrep]:
            self.parent[jrep] = irep 
        elif self.rank[irep] < self.rank[jrep]:
            self.parent[irep] = jrep

        else:
            self.parent[irep] = jrep
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
