# 680. Valid Palindrome II:

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""

# Steps: 2 - Pinters
# 1. Check if given two pointers are pallindrom
# 2. If Not:
#     i. check for i+1, j
#    ii. Check for i, j-1 sub string

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, i, j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i,j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return isPalindrome(s, i+1, j) or isPalindrome(s, i, j-1)
            i += 1
            j -= 1
        return True
      
      
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True      
