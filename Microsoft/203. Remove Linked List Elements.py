
'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''

# Solution 1: Using Iterative method Using Dummy Node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dum = ListNode(-1)
        curr = head
        prev = dum
        prev.next = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next  
            else:
                prev = curr
            curr = curr.next
        return dum.next
# Time: O(1)      
# Space: O(1)      
      
# Edge cases:
- The linked list is empty, i.e. the head node is None.
- Multiple nodes with the target value in a row.
- The head node has the target value.
- The head node, and any number of nodes immediately after it have the target value.
- All of the nodes have the target value.
- The last node has the target value.


        
