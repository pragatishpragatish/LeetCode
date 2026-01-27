class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        n = len(isConnected)
        count = 0

        def dfs(city):
            for nei in range(n):
                if nei not in seen and isConnected[city][nei] == 1:
                    seen.add(nei)
                    dfs(nei)

        for city in range(n):
            if city not in seen:
                dfs(city)
                count += 1

        return count