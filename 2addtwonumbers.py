#problem discription:

#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#1998 = 1000 + 900 + 90 +8  
#1 -> 9 -> 9 -> 8 

# 1998 % 10 = 8
# 1998 //10 =199 
#carry:
# 10 //10 =1  0-9 //10 =0

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0
        while (l1 or l2 or carry):
            val1 = (l1.val if l1 else 0)  
            val2 = (l2.val if l2 else 0)
            value = carry + val1 +val2    #get sum of v1+v2+carry
            
            result_tail.next=ListNode(value%10)
            carry = value //10
            result_tail = result_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next