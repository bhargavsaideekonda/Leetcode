class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for indices in range(len(nums)):
            for index in range(indices+1, len(nums)):
                if nums[indices] + nums[index] == target:
                    return [indices, index]