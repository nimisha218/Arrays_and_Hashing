class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
        #Initialize pointers
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle -1 
        return -1
            
        