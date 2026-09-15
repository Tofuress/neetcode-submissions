class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for i in strs:
            s = [0] * 26
            for j in i:
                s[ord(j) - 97] += 1
            if tuple(s) in dct:
                dct[tuple(s)].append(i)
            else:
                dct[tuple(s)] = [i]
        
        return list(dct.values())