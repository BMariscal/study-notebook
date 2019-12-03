from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = OrderedDict()  # use ordereddict to implement a queue/FIFO

    @property
    def is_at_capacity(self):
        return len(self.store) > self.capacity

    def get(self, key: int) -> int:
        try:
            self.store.move_to_end(key)  # move item to end
        except KeyError:
            return -1
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        self.store[key] = value
        self.store.move_to_end(key)  # move new item to end

        if self.is_at_capacity:
            self.store.popitem(last=False)  # pop first item in dict

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))  # returns 1
cache.put(1, 1)  # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
cache.put(4, 1)  # evicts key 1
print(cache.get(2))  # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))      # returns 4