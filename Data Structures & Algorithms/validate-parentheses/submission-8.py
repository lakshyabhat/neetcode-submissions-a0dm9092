class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for l in s:
            if l in para:
                stack.append(l)
            else:
                if stack:
                    p = stack.pop()
                    if para[p] != l:
                        return False
                else:
                    return False
        return False if len(stack) else True