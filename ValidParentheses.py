# Given a string contatining just the chars '(', ')', '{','}' '[',']', determine
# if string input is valid based on order of the  brackets

class Solution:
    def isValid(s: str) -> bool:
        st = []
        pairs = {"(":")","{":"}","[":"]"}
        for i in range(0, len(s)):
            if s[i] in pairs:
                st.append(s[i])
            else:
                if st != []:
                    if pairs[st[len(st)-1]] == s[i]:
                        st.pop()
                    else:
                        return False
                else:
                    return False
        if st == []:
            return True
        else:
            return False

    print(isValid("()"))