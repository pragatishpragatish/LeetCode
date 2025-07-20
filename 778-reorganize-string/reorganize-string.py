from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        pf, pc = 0, ""
        res = ""
        char_freq = Counter(s)

        for char, freq in char_freq.items():
            maxHeap.append((-freq, char))

        heapq.heapify(maxHeap)
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res += char

            if pf < 0:
                heapq.heappush(maxHeap, (pf, pc))

            freq += 1
            pf, pc = freq, char

        if len(res) != len(s):
            return ""

        return res