"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0: return ""

        last_bigger = 0
        last_str = ""

        dic = { }
        while  (True): # going through each letter
            i = 0
            for strc in strs:
                if i == 0 or strc in dic:
                    dic[strc] = dic.get(strc, 0) + 1
            i+=1
            # Removing low quantities
            maxQtt = max(qtt for qtt in dic.items())
            dic = { letter: qtt for letter, qtt in dic.items() if qtt == maxQtt }

            if (len(dic) in [0, 1]):
                break


        return dic.values()

print("['dog','racecar','car'] = '' and current is {val}".format(val=Solution().longestCommonPrefix(["dog","racecar","car"])))
print("['flower','flow','flight'] = 'fl' and current is {val}".format(val=Solution().longestCommonPrefix(["flower","flow","flight"])))