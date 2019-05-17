# Converts any roman number input from 1 - 3999

class Solution:
    def romanToInt(s: str) -> int:
        number = 0
        increment = False
        for i in range(0, len(s)):
            if increment == True:
                increment = False
            elif s[i] == 'I':
                number += 1
                if i != len(s)-1 and s[i+1] == 'V':
                    number += 3
                    increment = True
                elif i != len(s)-1 and s[i+1] == 'X':
                    number += 8
                    increment = True
            elif s[i] == 'V':
                number += 5
            elif s[i] == 'X':
                number += 10
                if i != len(s)-1 and s[i+1] == 'L':
                    number += 30
                    increment = True
                elif i != len(s)-1 and s[i+1] == 'C':
                    number += 80
                    increment = True
            elif s[i] == 'L':
                number += 50
            elif s[i] == 'C':
                number += 100
                if i != len(s)-1 and s[i+1] == 'D':
                    number += 300
                    increment = True
                elif i != len(s)-1 and s[i+1] == 'M':
                    number += 800
                    increment = True
            elif s[i] == 'D':
                number += 500
            elif s[i] == 'M':
                number += 1000
        return number

    print(romanToInt("III"))