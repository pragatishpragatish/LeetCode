class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda items: items[1])

        heap = []
        total = 0

        for duration, end in courses:
            total += duration
            heapq.heappush(heap, -duration)

            if total > end:
                total += heapq.heappop(heap)

        return len(heap)