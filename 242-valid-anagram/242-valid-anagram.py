class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Base Case
        if len(s) != len(t):
            return False
        
        # Else
        s_dict = {}
        t_dict = {}
        
        # Length of s and t is same
        for i in range(len(s)):
            
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
                
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        
        # Check if both the dictionaries are the same
        if s_dict != t_dict:
            return False
        else:
            return True

        
