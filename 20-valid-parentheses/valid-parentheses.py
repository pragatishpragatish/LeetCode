class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'[':']','{':'}','(':')'}

        for x in s:
            if x in ('({['):
                stack.append(x)
            else:
                if not stack:
                    return False
                if brackets[stack.pop()] != x:
                    return False

        return not stack