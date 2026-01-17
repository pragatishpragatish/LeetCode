class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter

        a = Counter(arr)
        n = len(arr)
        for x, y in a.items():
            if ((y/n) > 0.25):
                return x