class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        D = defaultdict(list)

        if source == destination:
            return True

        for a, b in edges:
            D[a].append(b)
            D[b].append(a)

        seen = set()

        def dfs(node):
            for x in D[node]:
                if x not in seen:
                    seen.add(x)
                    dfs(x)

        dfs(source)

        return destination in seen