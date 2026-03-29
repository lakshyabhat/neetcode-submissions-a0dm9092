class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            '}':'{',
            ']': '[',
            ')':'('
        }
        stack = []
        for p in s:
            if p in para:
                if stack and stack[-1] == para[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False