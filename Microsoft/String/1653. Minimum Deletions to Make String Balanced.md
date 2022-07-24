# 1653. Minimum Deletions to Make String Balanced:

<img width="735" alt="image" src="https://user-images.githubusercontent.com/35987583/166123093-96c877ae-3f89-40fa-b739-2f4728deaf19.png">




### Method 1: Using Stack and finding 'ba' sub string:

<img width="1161" alt="image" src="https://user-images.githubusercontent.com/35987583/166123111-ebb0b604-35e5-4589-8952-6ed8af416f46.png">

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        stack = []
        minDel = 0
        
        i = 0
        for ch in s:
            if len(stack) > 0 and stack[-1] == 'b' and ch == 'a':
                stack.pop()
                minDel += 1
            else:
                stack.append(ch)
        return minDel
```

Time: O(N)

Space: O(N)


# Method 2: At given poistion find 'a' in rightside and 'b' in leftside

We could delete all 'a's on the right hand side and all 'b's on the left hand side for any given point. So we just need to find the min(delete_cnt) as we keep updaing the a_cnt on the right hand side and b_cnt on the left hand side. The delete_cnt will be the a_cnt+b_cnt here.

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        aCount = 0
        for ch in s:
            if ch == 'a':
                aCount += 1
                
        bCount = 0    
        minDeletion = aCount + bCount
        
        for ch in s:
            if ch == 'a':
                aCount -= 1
            else:
                bCount += 1
                
            deletion = aCount + bCount
            minDeletion = min(minDeletion, deletion)
            
        return minDeletion
```
Time: O(N)

Space: O(1)
