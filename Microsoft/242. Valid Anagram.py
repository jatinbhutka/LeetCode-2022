"""


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# Solution 1: Using Dictionary (Add count of char, minus the count)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        #print (dic)
        
        for j in t:
            if (j not in dic) or dic[j] <= 0:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val >= 1:
                return False
        
        return True

# Time: O(N)
# Space: O(N)



