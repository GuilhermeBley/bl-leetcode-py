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
        totalRatings = len(ratings)
        currentCandyQuantity = 1
        leftSimblingCandyQuantity = { "quantity": 1, "rate": -1 }
        rightSimblingCandyQuantity = { "quantity": 1, "rate": -1 }
        ranges = [range(0, totalRatings - 1), reversed(range(0, totalRatings - 1))]
        answer = []

        for rangeSearch in ranges:
            for i in rangeSearch:
                currentCandyQuantity = 1
                currentRate = ratings[i]

                if (i < totalRatings - 1):
                    rightSimblingCandyQuantity = { "quantity": 1, "rate": ratings[i + 1] }

                try:
                    if (leftSimblingCandyQuantity["rate"] >= 0 and currentRate > leftSimblingCandyQuantity["rate"]): # is current rating bigger than the previous
                        currentCandyQuantity=leftSimblingCandyQuantity["quantity"] + 1

                    elif (currentRate > rightSimblingCandyQuantity["rate"]): # is current rating bigger than the next
                        currentCandyQuantity=rightSimblingCandyQuantity["quantity"] + 1
                finally:
                    if (len(answer) > i and i != 0):
                        answer[i] = max(answer[i], currentCandyQuantity)
                    else:
                        answer.insert(i, currentCandyQuantity)
                    leftSimblingCandyQuantity = { "quantity": currentCandyQuantity, "rate": currentRate }
        
        print(answer)
        return sum(answer)

            


print('' + str(Solution().candy([1,0,2])) + ' Expect: 5')
print('' + str(Solution().candy([1,2,2])) + ' Expect: 4')
print('' + str(Solution().candy([1,3,2,2,1])) + ' Expect: 7 Because => 1 + 2 + 1 + 2 + 1')
print('' + str(Solution().candy([1,2,87,87,87,2,1])) + ' Expect: 13 Because => 1 + 2 + 3 + 1 + 3 + 2 + 1')
print('' + str(Solution().candy([29,51,87,87,72,12])) + ' Expect: 12 Because => 1 + 2 + 3 + 2 + 2 + 1')
print('' + str(Solution().candy([1,6,10,8,7,3,2])) + ' Expect: 18 Because => 1 + 2 + 5 + 4 + 3 + 2 + 1')