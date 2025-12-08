class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        res = 0
        fuel = startFuel
        curr = 0

        stations.append([target, 0])

        for pos, fu in stations:
            dist = pos - curr

            while fuel < dist and heap:
                fuel += -heapq.heappop(heap)
                res += 1

            if fuel < dist:
                return -1
            
            fuel -= dist
            curr = pos
            heapq.heappush(heap, -fu)

        return res