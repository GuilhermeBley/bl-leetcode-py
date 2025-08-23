"""
OBS. NO SENSE PROBLEM. https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.
Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:
n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""

class Solution():
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        lastCandyQtt = 0
        amount = 0
        for i in range(0, len(ratings)):
            candy = 1
            if (i == 0): 
                amount += candy
                lastCandyQtt = candy
                continue
            lastKidRate = ratings[i-1]
            currentKidRate = ratings[i]

            if (currentKidRate > lastKidRate):
                candy = lastCandyQtt + 1
            
            lastCandyQtt = candy
            amount += candy

        return amount



r1 = Solution().candy([1,0,2])
print(r1) # should be 5, You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


r2 = Solution().candy([1,2,2])
print(r2) # should be 4, You can allocate to the first, second and third child with 1, 2, 1 candies respectively. The third child gets 1 candy because it satisfies the above two conditions.