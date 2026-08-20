from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])

        visited = [False]*n 
        visited[source] = True

        while q:
            node = q.popleft()

            if node == destination:
                return True 

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True 
                    q.append(nei)
        return False