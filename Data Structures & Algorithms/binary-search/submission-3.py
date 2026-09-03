class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1:
            return -1
        for i in range(round(len(nums) / 2)):
            if nums[i] == target:
                return i
            elif nums[-(i + 1)] == target:
                return len(nums) - i - 1
        return -1