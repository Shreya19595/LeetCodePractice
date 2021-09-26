#!/usr/bin/python

'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
'''


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        dummy = head
        while dummy:
            l.append(str(dummy.val))
            dummy = dummy.next
        num = "".join(l)
        
        value = int(num,2)
        return value
            
