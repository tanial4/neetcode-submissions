class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        else:
            stringb = "".join(char for char in s if char.isalnum())
            string = stringb.lower()

            i = 0
            j = len(string)-1

            while i < len(string)/2:
                if string[i] != string[j]:
                    return False

                i += 1
                j -= 1
            
            return True
        