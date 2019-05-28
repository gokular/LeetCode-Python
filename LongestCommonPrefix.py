# A function to find the longest common prefix among an array of strings.

class Solution:
    def longestCommonPrefix(strs) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ""
        prefix = strs[0]
        counter = 0
        size = len(prefix)
        for i in range(0, size):
            for j in range(1, len(strs)):
                if(prefix == strs[j][0:len(prefix)]):
                    counter += 1
            if(counter == len(strs)-1):
                return prefix
            else:
                prefix = prefix[0:-1]
                counter = 0
        return ""
    
    print(longestCommonPrefix(["Flower","Flight","Flamingo"]))