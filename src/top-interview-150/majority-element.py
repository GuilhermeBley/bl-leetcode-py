"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        keyWithMoreRecurrence = -1
        greatherNumber = 0


        for n in nums:
            currentCount = dic.get(n)

            if (currentCount):
                currentCount += 1
            else:
                currentCount = 1
            
            dic[n] = currentCount

            if (currentCount > greatherNumber):
                greatherNumber = currentCount
                keyWithMoreRecurrence = n

        return keyWithMoreRecurrence


nums = [2,2,1,1,1,2,2]
result = Solution().majorityElement(nums)

print(result)