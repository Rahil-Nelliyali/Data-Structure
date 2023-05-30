import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, nums):
        self.heap = nums[:]
        heapq.heapify(self.heap)

    def insert(self, num):
        heapq.heappush(self.heap, num)

    def remove(self, num):
        if num in self.heap:
            self.heap.remove(num)
            heapq.heapify(self.heap)

    def get_min(self):
        if self.heap:
            return self.heap[0]

    def print_heap(self):
        print(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, nums):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)

    def insert(self, num):
        heapq.heappush(self.heap, -num)

    def remove(self, num):
        if -num in self.heap:
            self.heap.remove(-num)
            heapq.heapify(self.heap)

    def get_max(self):
        if self.heap:
            return -self.heap[0]

    def print_heap(self):
        print([-num for num in self.heap])


# Example usage:

# Min Heap
min_heap = MinHeap()
min_heap.build_heap([3, 1, 4, 1, 5, 9, 2, 6, 8, 7])
min_heap.insert(0)
min_heap.remove(1)
min_heap.print_heap()
print("Minimum element:", min_heap.get_min())

# Max Heap
max_heap = MaxHeap()
max_heap.build_heap([3, 1, 4, 1, 5, 9, 2, 6, 8, 7])
max_heap.insert(10)
max_heap.remove(9)
max_heap.print_heap()
print("Maximum element:", max_heap.get_max())
