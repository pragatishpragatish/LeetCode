class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict, Counter

        if len(s1) > len(s2):
            return False
        a = Counter(s1)
        flag = False
        l, r = 0, len(s1)

        b = defaultdict(int)
        for i in range(r):
            b[s2[i]] += 1
        if a == b:
            return True
        

        for i in range(r, len(s2)):
            b[s2[i]] += 1
            b[s2[l]] -= 1
            if b[s2[l]] == 0:
                b.pop(s2[l])
            l += 1

            if a == b:
                return True
        return False