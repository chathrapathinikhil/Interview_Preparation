class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        a = x
        if x<0:
            return False
        else:
            while x:
                num = num * 10 + x % 10
                x = x // 10
            return True if num == a else False