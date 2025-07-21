import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        curr_max = float('-inf')
        for r in range(len(nums)):
            val = nums[r][0]
            heapq.heappush(heap, (val, r, 0))
            curr_max = max(curr_max, val)

        min_range = float('inf')
        start, end = -1, -1

        while heap:
            val, r, c = heapq.heappop(heap)
            
            if curr_max - val < min_range:
                min_range = curr_max - val
                start, end = val, curr_max

            if c + 1 < len(nums[r]):
                next_val = nums[r][c+1]
                heapq.heappush(heap, (next_val, r, c+1))
                curr_max = max(curr_max, next_val)
            else:
                break
        return [start,end]


        
