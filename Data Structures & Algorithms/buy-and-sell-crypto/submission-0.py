class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        new = prices[0]
        result = []

        for i in prices:
            if i <= new:
                new = i
            else:
                result.append(i - new)
            
            
            
        if result:
             return max(result)
        else:
             return 0
        