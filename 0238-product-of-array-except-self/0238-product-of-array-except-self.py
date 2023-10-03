class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create a preix array
        prefix = [[0] for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
    
        # Let's create a postfix array
        postfix = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            if i == (len(nums)-1):
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]
        
        # Let's start populating our result list
        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i+1])
            elif i == len(nums) - 1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * postfix[i+1])

        return result

















        # # Create two lists

        # # List1: The prefix list -> Store the product of the prefixes 

        # prefix = [0] * (len(nums))

        # for i in range(len(nums)):
        #     if (i==0):
        #         prefix[i] = nums[i]
        #     else:
        #         prefix[i] = nums[i] * prefix[i-1]
        
        # # List2: The postfix list -> Store the product of the postfixes

        # postfix = [0] * (len(nums))

        # for i in range(len(nums)-1, -1, -1):
        #     if i == len(nums) - 1:
        #         postfix[i] = nums[i]
        #     else:
        #         postfix[i] = nums[i] * postfix[i+1]
       
        # result = []

        # j = len(nums) - 1
        # for i in range(len(nums)):
        #     if i == 0:
        #         result.append(postfix[i+1])
        #     elif i == len(nums) - 1:
        #         result.append(prefix[j-1])
        #     else:
        #         result.append(postfix[i+1]*prefix[i-1])
        
        # return result
