class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {'[':']',
                    '{':'}',
                    '(':')'}
        currStack = []
        for para in s:
            if para not in pattern:
                if currStack and pattern[currStack[-1]] == para:
                    currStack.pop()
                else:
                    return False
            else:
                currStack.append(para)
        if currStack:
            return False
        return True
            