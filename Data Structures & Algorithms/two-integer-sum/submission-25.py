class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i, n in enumerate(nums):
            a = target - n
            if a in dct:
                return [dct[a], i]
            dct[n] = i