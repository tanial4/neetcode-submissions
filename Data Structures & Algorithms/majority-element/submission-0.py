class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        m = int(len(nums)/2)+1

        rep = Counter(nums)

        for key, value in rep.items():
            if value >= m:
                return key
        