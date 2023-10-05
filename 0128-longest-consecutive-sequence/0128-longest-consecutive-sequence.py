class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:


        numSet = set(nums)
        start = 0
        longest = 0

        for el in nums:

            if (el - 1) not in numSet:

                start = 0
            
                while (el + start) in numSet:
                    start += 1
                
                longest = max(start, longest)

        
        return longest


            





        

