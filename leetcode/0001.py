"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

# <================ Algorithm Method -- Brute force ======================>
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums) # Get the length of input array
        for i in range(n - 1):  # Outer loop: iterate through each element except the last one
            for j in range(i + 1, n):  # Inner loop: check all elements after nums[i]
                if nums[i] + nums[j] == target:   # If we find two numbers that sum to target, return their indices
                    return [i, j]
        return []
        # If no solution is found, return empty list
        # Time Complexity: O(n^2) where n is the length of nums
        # Space Complexity: O(1) as we only use two index variable

result = Solution().twoSum([1, 4, 2, 5], 7)
print(result)

