class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        
        res = []
        if len(p) > len(s):
            return res

        P = defaultdict(int)
        a = defaultdict(int)
        
        # Build freq for p
        for ch in p:
            P[ch] += 1
        
        # Build initial window
        l = 0
        r = len(p)
        for i in range(r):
            a[s[i]] += 1
        
        if a == P:
            res.append(0)
        
        # Slide window
        for i in range(r, len(s)):
            a[s[i]] += 1
            a[s[l]] -= 1
            
            # Remove zero counts so dicts match
            if a[s[l]] == 0:
                del a[s[l]]
            
            l += 1
            
            if a == P:
                res.append(l)
        
        return res
