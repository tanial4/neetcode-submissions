class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings = s.split(" ")

        for word in strings:
            if (len(word) != 0):
                print(word)
                n = len(word)

        return(n)