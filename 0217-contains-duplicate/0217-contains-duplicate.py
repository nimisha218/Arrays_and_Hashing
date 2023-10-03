class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        
        processed_numbers = set()

        for num in nums:
            if num not in processed_numbers:
                processed_numbers.add(num)
            else:
                return True
                
        return False

