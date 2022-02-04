# 92. Reverse Linked List II

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

```
- Divide problem in 3 steos:
 1. Reach out to left pointer.
 2. reverse linkedlist from left to right pointer
 3. connect nodes
```


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            # base case:
            if left == right:
                return head
            
            dum = left_prev = ListNode(-1, head)
            left_prev = dum
            curr = head
            
            for i in range(left-1):
                left_prev = left_prev.next
                curr = left_prev.next

            prev = None
            for i in range(right - left + 1):
                temp = curr.next   
                curr.next = prev
                prev = curr
                curr = temp

            left_prev.next.next = curr
            left_prev.next = prev
            
            return dum.next
          
# Time: O(N)
# Space: O(1)
