class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)

        for i in strs:
            s = [0] * 26
            for j in i:
                s[ord(j) - 97] += 1
            dct[tuple(s)].append(i)
        return list(dct.values())