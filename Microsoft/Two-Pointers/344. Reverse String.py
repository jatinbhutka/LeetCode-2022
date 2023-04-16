
# 344. Reverse String:

"""

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""

# Solution 1:


class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s) - 1
        for i in range(len(s)//2):
            s[i], s[j] = s[j], s[i]
            j = j - 1
            
# Time: O(N)
# space : O(1)



# Solution 2:

class Solution:
    def reverseString(self, s: List[str]) -> None:            
        
		# one points to head position, the other points to tail position
        left, right = 0, len(s)-1
        
		# reverse string by two pointers
        while left < right:
            
            s[left], s[right] = s[right], s[left]
            
            left,right = left+1, right-1
            
            
# Time: O(N)
# space : O(1)            
            


