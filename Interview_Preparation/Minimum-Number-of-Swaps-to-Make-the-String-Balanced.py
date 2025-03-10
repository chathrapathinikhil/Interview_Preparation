class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        for i in s:
            if i == ']' and unbalanced>0:
                unbalanced -= 1
            else:
                unbalanced+=1
        return unbalanced+1//2 if unbalanced%2==1 else unbalanced//2
