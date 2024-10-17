# 242. Valid Anagram:

How to sort String?

s = 'dcka'
sorted(s) ---> 'acdk'

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


```python
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
# Space: O(1) ----> Its Not O(N). Because we will be using constant space dic



# Solution 2: Using Sorting and comaparing


def isAnagram2(self, s, t):
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2

# Time: O(N)
# Space: O(1)    
    
    
    
# Solution 2: Using Sorting and comaparing
 
def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)
 
# Time: O(N Log N)
# Space: O(1)   

```



