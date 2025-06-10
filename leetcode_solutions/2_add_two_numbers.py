# https://leetcode.com/problems/add-two-numbers/description/
# 2025_06_10
# 1. Add Two Numbers
# Python

from typing import Optional # <- I need to better understand the use of Optional

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode()
        current_node = dummy_head
        sum = 0

        while l1 or l2 or sum:
            
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
            
            current_node.next = ListNode(sum % 10)
            sum //= 10
            current_node = current_node.next
        
        return dummy_head.next

sol = Solution()
list_one = [2, 4, 6]
list_two = [3, 5, 7, 9]
l1 = ListNode(list_one[0], ListNode(list_one[1], ListNode(list_one[2])))
l2 = ListNode(list_two[0], ListNode(list_two[1], ListNode(list_two[2], ListNode(list_two[3]))))
result = sol.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    print()
    result = result.next

