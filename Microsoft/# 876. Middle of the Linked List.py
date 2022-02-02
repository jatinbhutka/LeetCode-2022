# 876. Middle of the Linked List

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

# Solution 1: Two - Pointer

'''
Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
For example, head = [1, 2, 3, 4, 5], I bolded the slow and fast in the list.
step 0: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
step 1: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
step 2: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base Case:
        if head is None or head.next is None:
            return head
    
        # Using 2-pointer:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
      
   
# Solution 1: Using Counter
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Iter, N = head, 0
        while Iter:
            Iter, N = Iter.next, N + 1
        for i in range(N//2):
            head = head.next
        return head      
