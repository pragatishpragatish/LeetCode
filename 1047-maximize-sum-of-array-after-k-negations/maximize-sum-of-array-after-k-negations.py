class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        Heap = nums[:]
        heapq.heapify(Heap)

        for i in range(k):
            a = heapq.heappop(Heap)
            a = a * -1
            heapq.heappush(Heap, a)

        return sum(Heap)