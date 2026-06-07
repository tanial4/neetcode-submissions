class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        max_lenght = 0

        for rigth in range(len(s)):
            while s[rigth] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[rigth])
            max_lenght = max(max_lenght, rigth -left +1)
        
        return max_lenght