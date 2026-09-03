class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in dct:
                if stack and stack[-1] == dct[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False