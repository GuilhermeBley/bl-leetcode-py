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
        print("Row-by-Row Printing:")
        for i, row in enumerate(matrix):
            print(f"Row {i}: {row}")
        return 0
    
# Example usage:
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(Solution().trap([4,2,0,3,2,5]))  # Output: 9
