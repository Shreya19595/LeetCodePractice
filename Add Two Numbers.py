#!/usr/bin/python

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = ''
        p2 = ''

        while l1:
            p1 += str(l1.val)
            l1 = l1.next

        while l2:
            p2 += str(l2.val)
            l2 = l2.next

        p3 = int(p1[::-1]) + int(p2[::-1])
        p3 = str(p3)
        p = ListNode(int(p3[-1]))
        res = p

        for i in range(len(p3) - 2, -1, -1):
            p.next = ListNode(int(p3[i]))
            p = p.next

        return res 
