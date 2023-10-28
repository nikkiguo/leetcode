class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenStack = []
        parenDict = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char == '(' or char == '{' or char == '[':
                parenStack.append(char)
            else:
                if parenStack:
                    peek = parenStack[-1]
                    if parenDict.get(peek) != char:
                        return False
                    else:
                        parenStack.pop()
                else:
                    if char not in parenDict:
                        return False

        if not parenStack:
            return True

        return False
