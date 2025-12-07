class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = defaultdict(int)
        res = []
        si, e = 0, 0
        for i in range(len(s)):
            hash[s[i]] = i
        for i, c in enumerate(s):
            si += 1
            e = max(e, hash[c])

            if i == e:
                res.append(si)
                si = 0
        return res


        print(hash)