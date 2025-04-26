"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution(object):
    def productExceptSelf(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        allProd = 1
        zeroIndexes = []
        for i in range(0, len(nums)):
            n = nums[i]
            if (n == 0):
                zeroIndexes.append(i) 
                continue
            allProd *= n

        products = []
        for i in range(0, len(nums)):
            n = nums[i]

            if (len(zeroIndexes) > 1):
                products.append(0)
                continue

            if (len(zeroIndexes) == 1 and n != 0):
                products.append(0)
                continue

            if (n == 0 and len(zeroIndexes) == 1):
                products.append(allProd)
                continue

            products.append(allProd / n)

        return products
    
nums = [1,2,3,4]
r = Solution().productExceptSelf(nums)
print(r)