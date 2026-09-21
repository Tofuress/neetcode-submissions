class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        h = 0
        for i in nums:
            if i - 1 not in s:
                c = i
                l = 1
                while True:
                    c += 1
                    if c in s:
                        l += 1
                    else:
                        h = max(h, l)
                        break
        return h