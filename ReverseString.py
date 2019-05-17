class Solution:
    def reverseString(s) -> None:
        tempString = ''
        for i in range(0, len(s)):
            tempString += s[len(s)-1-i]
        for j in range(0, len(s)):
            s[j] = tempString[j]

    s = ["h","e","l","l","o"]
    reverseString(s)
    print(s)