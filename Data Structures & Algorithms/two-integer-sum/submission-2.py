class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Time complexity is O(n) we make a single pass through the array.
        Space complexity in worst case we store almost all elements in the dictionary"""
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            else:
                seen[x] = i

        return []