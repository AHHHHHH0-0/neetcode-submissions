class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = Counter(s1)
        count = defaultdict(int)
        target_len = len(s1)
        i = 0
        for j in range(len(s2)):
            count[s2[j]] += 1
            if s2[j] not in target_count:
                while i <= j:
                    count[s2[i]] -= 1
                    i += 1
                continue
            if count[s2[j]] > target_count[s2[j]]:
                while count[s2[j]] > target_count[s2[j]]:
                    count[s2[i]] -= 1
                    i += 1
                continue
            if j-i+1 == target_len:
                return True
        return False
            

                