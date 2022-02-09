# 21. Merge Two Sorted Lists:

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []
  
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

### Iterative:
### ============

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumm = ListNode(-101)
        prev = dumm
        prev.next = list1
        
        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next
            prev = prev.next
        
        prev.next = list1 if list1 else list2
        return dumm.next
    
    
    
# Complexity Analysis

# Time complexity : O(n + m)O(n+m)
# Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

# Space complexity : O(1)O(1)
#The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.    




### Recursive:
### ================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if (list1.val > list2.val): 
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
            else:  
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
              
              
# Complexity Analysis:

# Time complexity : O(n + m)O(n+m)
#Because each recursive call increments the pointer to l1 or l2 by one (approaching the dangling null at the end of each list), there will be exactly one call to mergeTwoLists per element in each list. Therefore, the time complexity is linear in the combined size of the lists.

# Space complexity : O(n + m)O(n+m)
# The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, so n + mn+m stack frames consume O(n + m)O(n+m) space.              
