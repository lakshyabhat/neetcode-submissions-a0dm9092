class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.size = size

    def next(self, val: int) -> float:
        self.arr.append(val)
        if self.size >len(self.arr):
            return sum(self.arr)/len(self.arr)
        return sum(self.arr[-self.size:])/self.size
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
