class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append('#')
            res.append(i)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i <= len(s) - 1:
            if s[i] == '#':
                num = int(s[:i])
                word = s[i + 1:i + num + 1]
                res.append(word)
                s = s[i + num + 1:]
                i = 0
            else:
                i += 1
        return res


