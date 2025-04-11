"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

from typing import List


class Solution(object):
    def rotate(self, nums: List[int], k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if (k > len(nums)):
            k = len(nums) - 1
        
        copy = nums[:k+1]
        del nums[:k+1]
        for c in copy:
            nums.append(c)


# [5,6,7,1,2,3,4]
nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)