class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        visited = set()
        left = 0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])
            maxLen = max(maxLen, i-left+1)
        return maxLen