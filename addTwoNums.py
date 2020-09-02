# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        pre = head
        carry = 0
        
        while(l1 and l2):
            total = l1.val + l2.val + carry
            carry = total // 10
            value = total % 10
            
            l1.val = value
            pre = l1
            l1 = l1.next
            l2 = l2.next
        
        rest = l1 if l1 else l2
        while(rest):
            total = rest.val + carry
            carry = total // 10
            value = total % 10
            pre.next = ListNode(value)
            pre = pre.next
            rest = rest.next
            
        if (carry):
            pre.next = ListNode(carry)
        return head