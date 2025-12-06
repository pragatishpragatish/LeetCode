class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        Len = len(pre)

        for x in strs[1:]:
            while pre != x[0:Len]:
                Len -= 1
                
                if Len == 0:
                    return ""

                pre = pre[0:Len]
        return pre
