class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        freq = dict()
        res = 0
        for r in range(len(s)):
            length = r - l + 1
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(freq[s[r]], maxf)
            if length - maxf <= k:
                res = max(res, length)
            else:
                while r - l + 1 - maxf > k:
                    freq[s[l]] -= 1
                    l += 1
        return res


    # AABAABAABAABBBABBBAA