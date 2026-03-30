class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for p in s:
            if p in para:
                stack.append(p)
            else:
                if not stack or para[stack.pop()] != p:
                    return False
        if len(stack):
            return False
        return True