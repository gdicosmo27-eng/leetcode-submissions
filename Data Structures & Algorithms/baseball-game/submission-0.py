class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i, str in enumerate(operations):
            if str.lstrip('-').isdigit():
                record.append(int(str))
            if str == "+" and len(record) > 1:
                record.append(record[-1] + record[len(record) - 2])
            if str == "D":
                if len(record) > 0:
                    record.append(2 * record[-1])
                else:
                    record.append(0)
            if str == "C" and len(record) > 0:
                record.pop()
        return sum(record)
                