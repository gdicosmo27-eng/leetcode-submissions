class MedianFinder:

    def __init__(self):
        self.small = [] # Max heap containing smaller half of numbers
        self.big = [] # Min heap containing larger half of numbers

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            if not len(self.small):
                heapq.heappush_max(self.small, num)
            elif num > self.small[0]:
                heapq.heappush(self.big, num)
            else:
                heapq.heappush_max(self.small, num)
        elif len(self.big) > len(self.small):
            if num > self.big[0]:
                tmp = heapq.heappop(self.big)
                heapq.heappush(self.big, num)
                heapq.heappush_max(self.small, tmp)
            else:
                heapq.heappush_max(self.small, num)
        else:
            if num < self.small[0]:
                tmp = heapq.heappop_max(self.small)
                heapq.heappush_max(self.small, num)
                heapq.heappush(self.big, tmp)
            else:
                heapq.heappush(self.big, num)

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            res = (self.small[0] + self.big[0]) / 2
            return res
        if len(self.small) > len(self.big):
            return float(self.small[0])
        return float(self.big[0])
        
        