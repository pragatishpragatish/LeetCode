class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a, b = 0, len(heights) - 1
        maxArea = 0
        for i in range(len(heights)):
            while a < b:
                if heights[a] < heights[b]:
                    maxArea = max(maxArea, (min(heights[a], heights[b]) * (b-a)))
                    a+=1
                else:
                    maxArea = max(maxArea, (min(heights[a], heights[b]) * (b-a)))
                    b-=1
        return maxArea