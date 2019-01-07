class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return self.size
    
    def dequeue(self):
        if not self.first: return
        temp = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.size -= 1
        return temp.value


# q = Queue()
# print(q.enqueue('First'))
# print(q.enqueue('Second'))
# print(q.enqueue('Third'))
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())