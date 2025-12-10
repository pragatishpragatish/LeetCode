class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i:[] for i in range(numCourses)}
        visited = set()

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):
            if node in visited:
                return False

            if graph[node] == []:
                if node not in res:
                    res.append(node)
                return True

            visited.add(node)
            for x in graph[node]:
                if not dfs(x):
                    return False
            visited.remove(node)
            graph[node] = []
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res