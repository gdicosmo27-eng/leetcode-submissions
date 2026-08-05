class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        res = len(position)
        cars = []
        for i, pos in enumerate(position):
            cars.append((pos, speed[i]))
        cars.sort(reverse=True)

        for pos, spd in cars:
            timeToTarg = (target - pos) / spd
            if stack:
                if timeToTarg <= stack[-1]:
                    res -= 1
                    stack.append(stack[-1])
                else:
                    stack.append(timeToTarg)
            else:
                stack.append(timeToTarg)
        return res
            
