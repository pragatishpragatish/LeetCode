class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        provinces = 0
        n = len(isConnected)

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        for city in range(n):
            if city not in seen:
                dfs(city)
                provinces += 1
        return provinces