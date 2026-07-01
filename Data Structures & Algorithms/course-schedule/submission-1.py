from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * (numCourses) # i th index gives the index of pre
        adj = [[] for _ in range(numCourses)]

        for u , v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        if not q:
            return False
        nodes_visited = 0

        while q:
            node = q.popleft()
            nodes_visited += 1
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return nodes_visited == numCourses    