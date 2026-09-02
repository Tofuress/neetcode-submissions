class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            flag = False
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    flag = True
                    break
            if flag:
                return flag
        return flag
