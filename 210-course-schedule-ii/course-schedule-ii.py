class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i:[] for i in range(numCourses)}
        visit = set()
        cycle = set()

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):
            if node in cycle:
                return False

            if node in visit:
                return True

            cycle.add(node)
            for x in graph[node]:
                if not dfs(x):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res