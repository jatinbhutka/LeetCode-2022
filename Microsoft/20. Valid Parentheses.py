'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', '}':'{', ']':'['}
        stack  = []
        for ch in s:
            if ch in ('(', '{', '['):
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != dic[ch]:
                    return False
                stack.pop()
            
        if len(stack) == 0:
            return True
        else:
            return False
                    
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1 :
            return False     
        if len(s) == 0:
            return True
        
        stack = []
        ref = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] != ref[c]:
                    return False
                else:
                    stack.pop()  
        if len(stack) == 0:
            return True
             
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []          
                    

class Solution(object):
	def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3
	
# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket        
