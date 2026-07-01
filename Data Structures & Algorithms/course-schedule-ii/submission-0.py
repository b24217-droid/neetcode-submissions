class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            return []
        nodes_visited = 0
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            nodes_visited += 1
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return res if nodes_visited == numCourses else []