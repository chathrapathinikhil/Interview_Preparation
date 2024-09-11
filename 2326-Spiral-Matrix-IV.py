# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        i, j = 0, 0
        matrix = [[-1]*n for _ in range(m)]
        top, bottom, left, right = 0, m-1, 0, n-1
        while head and top<=bottom and left<=right:
            for i in range(left, right+1):
                if head:
                    matrix[top][i]=head.val
                    head = head.next
            top+=1
            for i in range(top, bottom+1):
                if head:
                    matrix[i][right]=head.val
                    head = head.next
            right-=1
            for i in range(right, left-1, -1):
                if head:
                    matrix[bottom][i]=head.val
                    head = head.next
            bottom-=1
            for i in range(bottom, top-1, -1):
                if head:
                    matrix[i][left]=head.val
                    head = head.next
            left+=1
        
        return matrix
