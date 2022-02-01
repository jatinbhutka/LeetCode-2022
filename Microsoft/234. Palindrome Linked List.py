# 234. Palindrome Linked List:

'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''


# Solution 1: Using Stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next:
            stack = []
            curr = head
            while curr:
                stack.append(curr)
                curr = curr.next
            
            curr = head
            while curr and len(stack) > 0:
                val = stack.pop()
                if curr.val == val.val:
                    curr = curr.next
                else: 
                    return False
            if len(stack)==0:
                return True
            else: 
                return False
        else:
            return head
          
# Time: O(N)
# Space: O(N)



# Solution 1: Using Reverse LinkedList
'''
METHOD 2 (By reversing the list) This method takes O(n) time and O(1) extra space.

- Get the middle of the linked list.
- Reverse the second half of the linked list.
- Check if the first half and second half are identical.
- Construct the original linked list by reversing the second half again and attaching it back to the first half
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr=temp
        
        slow = head
        curr = prev
        while curr:
            if curr.val != slow.val:
                return False
            slow = slow.next
            curr = curr.next
        return True

# Time: O(N)
# Space: O(1)
