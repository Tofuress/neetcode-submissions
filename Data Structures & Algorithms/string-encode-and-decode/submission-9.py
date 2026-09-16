class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += i + '+' + str(len(i)) + '#'
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            if s[i] == '+':
                num = ''
                for j in s[i + 1:]:
                    if j.isnumeric():
                        num += j
                    elif j == '#':
                        break
                    else:
                        num = ''
                        break
                if num:
                    res.append(s[i - int(num):i])
        return res
