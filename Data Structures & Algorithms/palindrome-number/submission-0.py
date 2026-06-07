class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        c = 0
        b = len(s)

        if b == 1:
            return True

        while c < b:
            if s[c] != s[b-1]:
                return False
            
            c += 1
            b -= 1
        
        return True
        