class MyCalendar:
    
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.left = None
        self.right = None     

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.startTime and not self.endTime:
            self.startTime = startTime
            self.endTime = endTime
            return True
        
        if startTime >= self.endTime:
            if self.right:
                return self.right.book(startTime, endTime)
            self.right = MyCalendar()
            return self.right.book(startTime, endTime)
        elif endTime <= self.startTime:
            if self.left:
                return self.left.book(startTime, endTime)
            self.left = MyCalendar()
            return self.left.book(startTime, endTime)
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)