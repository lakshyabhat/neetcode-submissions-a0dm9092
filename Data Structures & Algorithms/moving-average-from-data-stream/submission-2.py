class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.size = size

    def next(self, val: int) -> float:
        size, arr = self.size,self.arr
        arr.append(val)
        window_sum = sum(arr[-size:])
        return window_sum/min(len(arr),size)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
