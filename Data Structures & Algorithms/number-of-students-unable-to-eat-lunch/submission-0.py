class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if len(students) == 0:
            return 0
        if len(sandwiches) == 0:
            return len(students)
        while True:
            if len(sandwiches) == 0:
                break
            if sum(students) == 0:
                if sandwiches[0] == 1:
                    break
            if sum(students) == len(students):
                if sandwiches[0] == 0:
                    break
            
            if sandwiches[0] == students[0]:
                del sandwiches[0]
                del students[0]
            else:
                students.append(students[0])
                del students[0]
        return len(students)
            
           
