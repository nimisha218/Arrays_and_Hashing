class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for key in count:
            freq[count[key]].append(key)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):

            if len(freq[i]) > 0:
                for f in freq[i]:
                    result.append(f)
                    if len(result) == k:
                        return result

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         # Create an empty dictionary to track the frequencies of the numbers
#         d = {}

#         nums.sort()
#         result = []

#         for number in nums:
#             if number not in d:
#                 d[number] = 1
#             else:
#                 d[number] += 1

#         # Sort the dictionary based on the values
#         sorted_frequency_dictionary = sorted(d.items(), key=lambda x:x[1])

#         # Decreasing order
#         sorted_frequency_dictionary.reverse()

#         for el in range(k):
#             result.append(sorted_frequency_dictionary[el][0])
        
#         return result
