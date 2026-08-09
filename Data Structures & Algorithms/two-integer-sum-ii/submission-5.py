class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(numbers):
            while j < len(numbers):
                num = numbers[i] + numbers[j]
                if num == target:
                    return [i+1, j+1]
                elif num > target:
                    break
                j += 1
            i += 1
            j = i + 1