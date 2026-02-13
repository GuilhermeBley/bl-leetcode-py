"""
Docstring for top-interview-150.length-of-last-word

58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

import re


class Solution():
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "".join(s)
        return len(s.rstrip(' ').split(' ')[-1])
    
print("Example 1: 'Hello World' Should be 5, Current: {number}".format(number = Solution().lengthOfLastWord("Hello World")))
print("Example 2: '   fly me   to   the moon  ' Should be 4, Current: {number}".format(number = Solution().lengthOfLastWord("   fly me   to   the moon  ")))
print("Example 3: 'luffy is still joyboy' Should be 6, Current: {number}".format(number = Solution().lengthOfLastWord("luffy is still joyboy")))
print("Example 4: 'oneword' Should be 7, Current: {number}".format(number = Solution().lengthOfLastWord("oneword")))
print("Example 5: '' Should be 0, Current: {number}".format(number = Solution().lengthOfLastWord("")))