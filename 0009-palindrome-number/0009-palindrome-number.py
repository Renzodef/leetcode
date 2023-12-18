class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            num = x
            reverse = 0
            while num != 0:
                digit = num % 10
                reverse = reverse * 10 + digit
                num //= 10
            return reverse == x
