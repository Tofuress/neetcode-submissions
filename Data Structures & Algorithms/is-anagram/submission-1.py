class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}

        for i in s:
            s_dict[i] = 1 + s_dict.get(i, 0)
        
        for i in t:
            t_dict[i] = 1 + t_dict.get(i, 0)

        return t_dict == s_dict
        