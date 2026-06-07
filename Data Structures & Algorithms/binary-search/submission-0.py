class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        rigth = len(nums)-1
        

        while left <= rigth:
            mid = (rigth+left)//2 
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid +1
            else:
                rigth = mid -1 
            
        return -1
        