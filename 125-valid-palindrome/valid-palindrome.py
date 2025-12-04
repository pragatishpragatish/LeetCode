class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for a in s:
            if a.isalnum():
                s1 += a.lower()
        l, r = 0, len(s1)-1
        while l < r:
            if s1[r] != s1[l]:
                return False
            l += 1
            r -= 1
        return True