class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        processed_numbers = set()
        
        for element in nums:
            if element in processed_numbers:
                return True
            else:
                processed_numbers.add(element)
        return False


