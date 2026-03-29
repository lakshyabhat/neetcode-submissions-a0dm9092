class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            '}':'{',
            ']': '[',
            ')':'('
        }
        stack = []
        for p in s:
            lastPara = ''
            if p in para:
                if len(stack):
                    lastPara = stack.pop()
                if  lastPara!= para[p]:
                    return False
            else:
                stack.append(p)
        if len(stack):
            return False
        return True