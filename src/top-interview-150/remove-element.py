from typing import List


class Solution():
    def removeElement(self, nums: List[int], val: int):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        removedQtt = 0
        while (val in nums):
            nums.remove(val)
            removedQtt+=1

        qttNotMatched = len(nums)
        for i in range(removedQtt):
            nums.append(None)
        
        return qttNotMatched
        

nums = [3,2,2,3]
val = 3
k = Solution().removeElement(nums=nums, val=val)

print(k)
print(' - ')
print(nums)