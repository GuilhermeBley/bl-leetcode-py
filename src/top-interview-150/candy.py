"""
135. Candy Hard

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2] -- candy distribuition [2, 1, 2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2] -- candy distribuition [1, 2, 1]
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
        candyQtt = 0
        totalRatings = len(ratings)
        candyQuantity = 1
        for i in range(0, totalRatings):
            try:
                currentRate = ratings[i]
                if ((i > 0 and ratings[i-1] < currentRate) or (i < totalRatings - 1 and currentRate > ratings[i+1])):
                    candyQuantity+=1
                else:
                    candyQuantity = 1 # reseting quantity
            finally:
                candyQtt+=candyQuantity
        
        return candyQtt

            


print('' + str(Solution().candy([1,0,2])) + ' Expect: 5')
print('' + str(Solution().candy([1,2,2])) + ' Expect: 4')
print('' + str(Solution().candy([1,3,2,2,1])) + ' Expect: 7 Because => 1 + 2 + 1 + 2 + 1')
print('' + str(Solution().candy([1,2,87,87,87,2,1])) + ' Expect: 13 Because => 1 + 2 + 3 + 1 + 3 + 2 + 1')