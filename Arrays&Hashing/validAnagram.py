class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        obj1, obj2 = {}, {}

        for i in range(len(s)):
            obj1[s[i]] = 1 + obj1.get(s[i],0)
            obj2[t[i]] = 1 + obj2.get(t[i],0)

        return obj1 == obj2

        
