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
0 -> 4 -> 8 -> 12 -> (numRows * 2 - 2 = 4)
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
0 -> 6 -> 12 (+6) (numRows * 2 - 2 = 6)
1 -> 5 -> 7 -> 11 -> 13 (+4, +2, ...) (numRows + )
2 -> 4 -> 8 -> 10 (+2, +4, ...)
3 -> 9 (+6)

Example 3:
Input: s = "PAYPALISHIRING", numRows = 5
Output: "PINALSIGYAHRPI"
Explanation:
P       H 
A     S   I
Y   I       R
P L           I   G
A               N

0   1   2   3   4   5   6   7   8   9   10  11  12  13
P   A   Y   P   A   L   I   S   H   I   R   I   N   G
x   x   x   x   s   x   x   x   x   x   x   x   s   s
Index walk: 
0 -> 8 (numRows * 2 - 2 = 6)
1 -> 7 -> 9 -> 
2 -> 6 -> 10 ->
3 -> 5 -> 11 -> 13
4 -> 12 (numRows * 2 - 2 = 6)

Example 4:
Input: s = "A", numRows = 1
Output: "A"
"""

class Solution(object):

    def converToZigZagIndex(self, index, previous_zigzag_index, num_rows, total_text) -> int:
        lastIndex = total_text-1
        if (lastIndex < 1): return 0

        if (index == 0): return 0

        safe_non_zero = 1
        walk_size = num_rows * 2
        current_row_multiplier = (previous_zigzag_index + walk_size) % num_rows + safe_non_zero
        walk_for_index = int(walk_size / current_row_multiplier)
        return (previous_zigzag_index + walk_for_index) % (total_text - 1)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        newS = ""
        total_length = len(s)
        previous_index = 0
        for i in range(0, total_length):
            c_index = self.converToZigZagIndex(index=i, previous_zigzag_index=previous_index, num_rows=numRows, total_text=total_length)
            newS += s[c_index]
            previous_index = c_index

        return newS
        
        
print(Solution().convert("PAYPALISHIRING", 3)) #PINALSIGYAHRPI

"""
P     I    N
A   L S  I G
Y A   H R
P     I
"""