import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -x)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            if a != b:
                dif = a - b
                heapq.heappush(heap, -dif)
        
        if heap:
            return -heap[0]
        else:
            return 0
