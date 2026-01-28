"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution():
    def trapOptimized(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        holes = 0
        rows, cols = max(height), len(height)
        for i in range(rows):
            possible_holes = 0
            previous_elevation_index = -1
            for j in range(cols):
                elevation_size = height[j]
                is_elevation = elevation_size >= i + 1
                if (is_elevation and previous_elevation_index == -1):
                    previous_elevation_index = j
                elif (is_elevation):
                    holes = holes + (j - (previous_elevation_index + 1))
                    previous_elevation_index = j


        # TODO: Optimize runtime and space complexity
        return holes
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rows, cols = max(height), len(height)
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                elevation_size = height[j]
                isColumnFilled = elevation_size >= i + 1
                matrix[i][j] = isColumnFilled and 1 or 0

        holes = 0
        for i in range(rows):
            previous_elevation_index = -1
            for j in range(cols):
                is_elevation = matrix[i][j] == 1
                if (is_elevation and previous_elevation_index == -1):
                    previous_elevation_index = j
                elif (is_elevation):
                    holes = holes + (j - (previous_elevation_index + 1))
                    previous_elevation_index = j

        # TODO: Optimize runtime and space complexity
        return holes
    
# Example usage:
print(Solution().trapOptimized([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(Solution().trapOptimized([4,2,0,3,2,5]))  # Output: 9