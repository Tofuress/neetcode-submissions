class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^\w]", "", s).lower()
        return s == s[::-1]