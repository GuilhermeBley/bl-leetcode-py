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

        dic = { }
        i = 0
        while  (True): # going through each letter
            for strc in strs:
                if i < len(strc):
                    key = strc[i]
                    dic[key] = dic.get(key, 0) + 1
            
            if (len(dic) == 0): return ""

            # Removing low quantities
            maxQtt = max(qtt for _,qtt in dic.items())
            dic = { letter: qtt for letter, qtt in dic.items() if qtt == maxQtt }
                        
            availableletters = [st for st,_ in dic.items()]
            oldstrs = strs
            strs = [st for st in strs if len(st) > 0 and i < len(st) and st[i] in availableletters]
            if (len(oldstrs) > len(strs) and i > 0):
                return oldstrs[0][0:i]
            if (len(strs) == 1):
                return strs[0]
            if (len(strs) == len(dic)):
                return "" # all letters are different
            
            dic = { }
            i+=1
            if (len(strs) == 0):
                break
        
        return ""


print("['a'] = 'a' and current is '{val}'".format(val=Solution().longestCommonPrefix(["a"])))
print("['dog','racecar','car'] = '' and current is '{val}'".format(val=Solution().longestCommonPrefix(["dog","racecar","car"])))
print("['flower','flow','flight'] = 'fl' and current is '{val}'".format(val=Solution().longestCommonPrefix(["flower","flow","flight"])))
print("['gol','gol bola', 'flower','flow','flight'] = 'flo' and current is '{val}'".format(
    val=Solution().longestCommonPrefix(["gol", "gol bola", "flower","flow","floght"])))