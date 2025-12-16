class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        a, b = len(word1), len(word2)

        l1, l2 = 0, 0

        while l1 < a or l2 < b:
            if l1 < a:
                res.append(word1[l1])
                l1 += 1
            if l2 < b:
                res.append(word2[l2])
                l2 += 1
        return "".join(res)