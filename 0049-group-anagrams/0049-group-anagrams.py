class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        main_d = {}

        for word in strs:

            # Let's create an empty dictionary
            d = {chr(letter): 0 for letter in range(97, 123)}
            
            for w in word:
                if w in d:
                    d[w] += 1
            
            if str(d.values()) not in main_d:
                main_d[str(d.values())] = [word]
            else:
                main_d[str(d.values())].append(word)
        
        return main_d.values()
            


        
        
        
        




















        
        
        
        

#         # Let's create an empty dictionary:
#         d = {}

#         # Let's iterate over each word in the list
#         for word in strs:

#             main_d = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g":0, "h": 0, "i": 0, "j": 0, "k": 0, "l":0, "m":0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

#             for w in word:
#                 if w in main_d:
#                     main_d[w] = main_d[w] + 1
            
#             if tuple(main_d.values()) not in d:
#                 d[tuple(main_d.values())] = [word]
#             else:
#                 d[tuple(main_d.values())].append(word)

#         return d.values()





























        # d = {}

        # for el in strs:
        #     if str(sorted(el)) not in d:
        #         d[str(sorted(el))] = [el]
        #     else:
        #         d[str(sorted(el))].append(el)
        
        # return d.values()



        # output = []
        # if len(strs) == 1:
        #     output.append(strs)
        #     return output
        # while len(strs) > 1:
        #     for el1 in strs:
        #         result = []
        #         result.append(el1)
        #         if el1 in strs:
        #             strs.remove(el1)
        #         for el2 in strs[:]:
        #             if sorted(el1) == sorted(el2):
        #                 result.append(el2)
        #                 strs.remove(el2)
        #         if len(result) != 0:
        #             output.append(result)
        #         if len(strs) == 1:
        #             output.append(strs)
        # return output































        # result = []
        # output = []

        # for i in range(len(strs)):

        #     if strs[i] == "xxx":
        #         continue

        #     temp = [strs[i]]
            

        #     for j in range(i+1, len(strs)):
                
        #         if strs[j] == "xxx":
        #             continue

        #         if sorted(strs[i]) == sorted(strs[j]):
        #             temp.append(strs[j])
        #             strs[j] = "xxx"
            
        #     result.append(temp)

        # for r in result:
        #     if "xxx" not in r:
        #         output.append(r)
    
        # print(output)

        # return output










