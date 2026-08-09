class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        seen = set()
        for i, l in enumerate(s):
            if l not in seen:
                seen.add(l)
                res = max(res, i-start+1)
            else:
                while s[start] != l:
                    seen.remove(s[start])
                    start += 1
                start += 1
        return res
            

