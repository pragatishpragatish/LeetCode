from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        res = ""
        count = Counter(s)
        for char, freq in count.items():
            heap.append((-freq, char))

        heapq.heapify(heap)
        while heap:
            freq, char = heapq.heappop(heap)
            res += char * (-freq)

        return res