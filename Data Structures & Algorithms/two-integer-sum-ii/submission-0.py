class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_1 = 0
        p_2 = len(numbers) - 1

        while True:
            if numbers[p_1] + numbers[p_2] > target:
                p_2 -= 1
            elif numbers[p_1] + numbers[p_2] < target:
                p_1 += 1
            else:
                return [p_1 + 1, p_2 + 1]