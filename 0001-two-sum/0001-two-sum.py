class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i, n in enumerate(nums):

            difference = target - n 
            if n in d:
                return [d[n], i]
            d[difference] = i
            
        return

























        
        # # Create an empty dictionary
        # d = {}
        
        # # i->index, n-> num
        # for i, n in enumerate(nums):
        #     difference = target - n
        #     if difference in d:
        #         return [d[difference], i]
        #     d[n] = i
        # return
            
            
        
                
            