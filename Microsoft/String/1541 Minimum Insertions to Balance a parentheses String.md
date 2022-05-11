# 1541 Minimum Insertions to Balance a parentheses String:

![image](https://user-images.githubusercontent.com/35987583/167792486-97ddb593-ea30-4184-8098-45c5e4a51916.png)

# Using Stack:
        ## RC ##
        ## APPROACH : STACK ##
        ## LOGIC ##
        ## 1. Only 3 conditions, open brace -> push to stack
        ## 2. 2 close braces -> pop from stack, if you donot have enough open braces before increment count(indicates one open required)
        ## 3. Only 1 close brace found --> count + 1, to make it 2 close braces, if stack then just pop, if stack is empty then increment count by 2 (one for close brace, one for open brace)
        ## 4. If stack is still left with open braces, we require close braces = twice of that open braces in stack
        
        ## You can even optimize it, without using stack, just counting the left braces.
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        minInsertion = 0
        i = 0
        left = 0
        
        s = s + '$'
        
        while i < len(s) - 1:

            if s[i] == "(":
                left += 1
                i += 1
                
            elif s[i] == ')' and s[i+1] == ')':
                if left > 0:
                    left -= 1
                else:
                    minInsertion += 1
                i += 2
                
            elif s[i] == ')' and s[i+1] != ")":
                if left > 0:
                    left -= 1
                    minInsertion += 1
                else:
                    minInsertion += 2
                i += 1
           
        return minInsertion + left*2
```
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

# Using Stack
```python
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        minInsertion = 0
        
        for c in s:
            
            # c = "(":
            if c == '(':
                if len(stack) == 0:
                    stack.append(c)
                else:
                    stackTop = stack[-1]
                    if stackTop == '(':
                        stack.append(c)
                    else:
                        minInsertion += 1
                        stack.pop()
                        stack.pop()
                        stack.append(c)
            
            # c == ')'
            else:
                if len(stack) == 0:
                    minInsertion += 1
                    stack.append('(')
                    stack.append(c)
                else:
                    if stack[-1] == '(':
                        stack.append(c)
                    else:
                        stack.pop()
                        stack.pop()
                        
        if len(stack) == 0:
            return minInsertion
        else:
            while len(stack) > 0:
                stackTop = stack.pop()
                if stackTop == "(":
                    minInsertion += 2
                else:
                    minInsertion += 1
                    stack.pop()
                    
        return minInsertion
        
```
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
