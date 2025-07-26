class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        ans = set()
        l = 0
        for r in range(len(s)):
            while s[r] in ans:
                ans.remove(s[l])
                l += 1
            ans.add(s[r])
            res = max(res, (r-l+1))
        return res