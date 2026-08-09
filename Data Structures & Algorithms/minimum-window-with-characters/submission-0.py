class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        match = len(t)
        i = 0
        res = ""
        for j in range(len(s)):
            if s[j] in c:
                if c[s[j]] > 0:
                    match -= 1
                c[s[j]] -= 1

            while match == 0:
                if not res or j-i+1 < len(res):
                    res = s[i:j+1]
                if s[i] in c:
                    c[s[i]] += 1
                    if c[s[i]] > 0:
                        match += 1

                i += 1
        return res


        