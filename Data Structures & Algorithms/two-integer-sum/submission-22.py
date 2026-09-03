class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i, n in enumerate(nums):
            a = target - n
            if a in dct:
                return [min([i, dct[a]]), max([i, dct[a]])]
            dct[n] = i