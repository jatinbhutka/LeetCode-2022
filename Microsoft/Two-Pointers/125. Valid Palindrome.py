# 125. Valid Palindrome:

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# Solution1: 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=''
        for ch in s:
            if ch.isalnum():
                ch.lower()
                ns += ch
        return ns.lower()[::-1] == ns.lower()   
      
# Time: O(N)
# Space: O(N)


class Solution:
    def isPalindrome(self, s: str) -> bool:
    	s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]
    
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
    	i, j = 0, len(s) - 1
    	while i < j:
    		a, b = s[i].lower(), s[j].lower()
    		if a.isalnum() and b.isalnum():
    			if a != b: return False
    			else:
    				i, j = i + 1, j - 1
    				continue
    		i, j = i + (not a.isalnum()), j - (not b.isalnum())
    	return True  
    
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
    
# Time: O(N)
# Space: O(1)
        
