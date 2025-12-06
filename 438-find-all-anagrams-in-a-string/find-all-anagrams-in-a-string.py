class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        res = []
        countP = Counter(p)
        l, r = 0, len(p)
        while r<len(s)+1:
            tempCount = Counter(s[l:r])
            if tempCount == countP:
                res.append(l)
            l += 1
            r += 1

        return res