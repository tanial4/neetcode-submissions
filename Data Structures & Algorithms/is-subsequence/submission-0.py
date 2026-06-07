class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r = ''
        i = 0
        j = 0

        if len(s) <= len(t):
            if s == "":
                return True
            else:
                while i < len(t) and j < len(s):
                    if s[j] == t[i]:
                        r += t[i]
                        j += 1
                    i += 1
                if r == s:
                    return True
                else:
                    return False

        else:
            return False
        