class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = Counter(s1)
        count = defaultdict(int)
        target_len = len(s1)
        i = 0
        for j, letter in enumerate(s2):
            count[letter] += 1
            while count[letter] > target_count[letter]:
                count[s2[i]] -= 1
                i += 1
            if j-i+1 == target_len:
                return True
        return False
            

                