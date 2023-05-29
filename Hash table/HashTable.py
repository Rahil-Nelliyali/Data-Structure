class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for entity in self.table[index]:
            if entity[0] == key:
                entity[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for entity in self.table[index]:
            if entity[0] == key:
                return entity[1]
        raise KeyError(key)

    def remove(self, key):
        index = self.hash_function(key)
        for i, entity in enumerate(self.table[index]):
            if entity[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

    def print(self):
        print(self.table)


obj = Hashtable(10)
obj.insert(10, 25)
obj.insert(34, 67)
obj.remove(10)
obj.print()
