class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = OrderedDict()
        self.size = 0

    def get(self, key: int) -> int:
        tmp = self.hashmap.get(key, -1)
        if tmp != -1:
            self.hashmap.move_to_end(key)
        return tmp

    def put(self, key: int, value: int) -> None:
        if self.hashmap.get(key, -1) != -1:
            self.hashmap[key] = value
            self.hashmap.move_to_end(key)
        else:
            self.hashmap[key] = value
            self.size += 1
            if self.size > self.capacity:
                self.hashmap.popitem(last=False)
                self.size -= 1
            


