# Takes in any int and reverses the order of it. If the inputted number is
# negative, then negative is kept at the begninning. Only 32-bit numbers are accepted.

class Solution:
    def reverse(x: int) -> int:
        if(x < -2147483648 or x > 2147483647):
            return 0
        stringNumber = str(x)
        if(stringNumber[0] != '-'):
            numberArray = str(x)[::-1]
            result = int(numberArray)
            if(result < -2147483648 or result > 2147483647):
                return 0
            return result
        else:
            stringNumber = stringNumber[1:len(str(x))]
            numberArray = stringNumber[::-1]
            result = int('-' + numberArray)
            if(result < -2147483648 or result > 2147483647):
                return 0
            return result
    
    print(reverse(123))
