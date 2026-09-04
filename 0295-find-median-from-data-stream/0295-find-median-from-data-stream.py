class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()
        n = len(self.l)

        if n%2 != 0:
            return float(self.l[n//2])
        mid  = n // 2
        return (self.l[mid - 1] + self.l[mid]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()