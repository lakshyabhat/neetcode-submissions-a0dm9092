class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []
        for o in operations:            
            if o == '+':
                if scoreStack:
                    prev = scoreStack[-1]
                    curr = scoreStack[-2]
                    scoreStack.append(prev + curr)
            elif o == 'C':
                if scoreStack:
                    scoreStack.pop()
            elif o == 'D':
                if scoreStack:
                    scoreStack.append(scoreStack[-1]*2)
            else:
                val = int(o)
                if val<0:
                    scoreStack.append(val)
                else:
                    scoreStack.append(val)
        print(scoreStack)
        if scoreStack:
            return sum(scoreStack)
        return 0