class BinaryHeapMax:
    def __init__(self):
        self.values = []
    
    def insert(self, value):
        self.values.append(value)
        self.bubbleUp()
    
    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx - 1)//2
            if element <= self.values[parentIdx]: 
                break
            self.values[idx] = self.values[parentIdx]
            self.values[parentIdx] = element
            idx = parentIdx;

heap = BinaryHeapMax()
lista = [33,18,39,41,27,12,55]

for e in lista:
    heap.insert(e)
print(heap.values)