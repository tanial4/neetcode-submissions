class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        u = dict()

        for i in range(len(s)):
            u[s[i]] = u.get(s[i],0)+1
            u[t[i]] = u.get(t[i],0)-1               

        for value in u.values():
            if value != 0:
                return False
        return True
        