# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0)
        temp, temp1 = head, dummy
        count = 1
        while temp:
            print(stack)
            if count%2 == 1:
                stack.append(temp.val)
                temp = temp.next
                count+=1
                continue
            temp1.next = ListNode(temp.val)
            temp1 = temp1.next
            temp1.next = ListNode(stack.pop())
            count+=1
            temp1 = temp1.next
            temp = temp.next
        if stack:
            temp1.next = ListNode(stack.pop())
        return dummy.next
