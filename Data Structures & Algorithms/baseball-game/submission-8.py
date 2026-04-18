class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []
        for o in operations:            
            if o == '+':
                prev = scoreStack[-1]
                curr = scoreStack[-2]
                scoreStack.append(prev + curr)
            elif o == 'C':
                scoreStack.pop()
            elif o == 'D':
                scoreStack.append(scoreStack[-1]*2)
            else:
                val = int(o)
                scoreStack.append(val)
        print(scoreStack)
        if scoreStack:
            return sum(scoreStack)
        return 0