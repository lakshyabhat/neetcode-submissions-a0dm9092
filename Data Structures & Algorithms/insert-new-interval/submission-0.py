class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            s,e = interval[0],interval[1]
            new_s, new_e = newInterval[0],newInterval[1] 
            if e>=new_s:
                if new_e>= s:
                    res_s,res_e = min(s,new_s), max(e,new_e)
                    newInterval = [res_s,res_e]
                else:
                    res.append([new_s,new_e])    
                    newInterval = [s,e]
            else:
                res.append([s,e])
        res.append(newInterval)
        return res

