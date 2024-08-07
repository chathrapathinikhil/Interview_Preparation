# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        carry = 0
        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            res = val1 + val2 + carry
            carry = res//10
            res = res%10
            temp.next = ListNode(res)
            temp = temp.next
            print(temp)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return head.next