from collections import OrderedDict
class LRU(OrderedDict):
    def __init__(self, capacity):
        self.capacity=capacity

    def get(self, key):
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)