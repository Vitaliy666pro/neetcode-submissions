class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """brute force solution with O(n**2) complexity and O(1) space"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        