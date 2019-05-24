# Checks whether or not a given number is a palindrome

class Solution:
    def isPalindrome(x: int) -> bool:
        strNumber = str(x)
        strNumberR = str(x)[::-1]
        if strNumber == strNumberR:
            return True
        else:
            return False
    
    print(isPalindrome(121))
