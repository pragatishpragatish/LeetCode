class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        freq = Counter(text)
        print(freq)
        res = 0
        
        
        for char in set(text):
            left = 0
            count = 0

            for right in range(n):
                if text[right] != char:
                    count += 1

                while count > 1 or (right - left + 1) > freq[char]:
                    if text[left] != char:
                        count -= 1

                    left += 1

                res = max(res, right - left + 1)

        return res