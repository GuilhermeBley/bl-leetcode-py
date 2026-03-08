"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
See the letters flow direction:
⬇️🟥⬆️🟥⬆️🟥⬆️...
⬇️⬆️⬇️⬆️⬇️⬆️⬇️...
⬇️🟥⬇️🟥⬇️🟥⬇️...
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
⬇️🟥⬆️🟥⬆️🟥⬆️...
⬇️⬆️⬇️⬆️⬇️⬆️⬇️...
⬇️🟥⬇️🟥⬇️🟥⬇️...
0   1   2   3   4   5   6   7   8   9   10  11  12  13
P   A   Y   P   A   L   I   S   H   I   R   I   N   G
Index walk: 
0 -> 4 -> 8 -> 12 -> (+4)
1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 13 (+2)
2 -> 6 -> 10 (+4)

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

0   1   2   3   4   5   6   7   8   9   10  11  12  13
P   A   Y   P   A   L   I   S   H   I   R   I   N   G
s   s   s   s   s   s   s   s   s   x   s   s   s   x
Index walk: 
0 -> 6 -> 12 (+6)
1 -> 5 -> 7 -> 11 -> 13 (+4, +2, ...)
2 -> 4 -> 8 -> 10 (+2, +4, ...)
3 -> 9 (+6)

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
print(Solution().convert("PAYPALISHIRING", 3))