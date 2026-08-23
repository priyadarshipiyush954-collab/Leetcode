class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        halfRev = 0

        while halfRev < x:
            halfRev = halfRev * 10 + (x % 10)
            x //= 10

        return halfRev == x or halfRev // 10 == x
        