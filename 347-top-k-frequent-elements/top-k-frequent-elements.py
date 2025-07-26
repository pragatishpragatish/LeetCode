from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = []
        res = []
        for num, freq in count.items():
            maxHeap.append((-freq, num))

        heapq.heapify(maxHeap)
        
        for _ in range(k):
            freq, num = heapq.heappop(maxHeap)
            res.append(num)
        return res