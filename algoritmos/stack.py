# Pilhas: first in first out -> FIFO

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.size = 0;
        self.first = None
        self.last = None
        self._lista = []
    
    def push(self, value):
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        self.size += 1
        return self.size

    def pop(self):
        if not self.first: return
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.size -= 1
        return temp.value
    
    def __getitem__(self, key):
        return []
