class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for l1 in s:
            if l1 in dict1:
                dict1[l1] += 1
            else: 
                dict1[l1] = 1
        for l2 in t:
            if l2 in dict2:
                dict2[l2] += 1
            else:
                dict2[l2] = 1
        if dict1 != dict2:
            return False
        return True
        