class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        node = Node(val)
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next =  node
            self.tail = node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return self.tail

    def get(self, index):
        if index < 0 or self.length - 1 < index:
            return None
        current = self.head
        count = 0
        if index < self.length/2:
            while count != index:
                current = current.next
                count += 1
        else:
            count = self.length - 1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1
        return current

    def unshift(self, val):
        node = Node(val)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1
        return self

    def shift(self):
        if self.length == 0:
            return 
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return self

    def set(self, index, val):
        current = self.get(index)
        if current == None:
            return
        current.val = val

    def delete(self, index):
        current = self.get(index)
        if current == None:
            return False
        if index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()

        prev = current.prev
        aft = current.next
        current = None
        prev.next = aft
        aft.prev = prev

        self.length -= 1

        return True

    def print(self):
        if self.length == 0:
            print('vazio...')
        else:
            p = ''
            current = self.head
            while current.next:
                p += str(current.val) + ' <--> '
                current = current.next
            p += str(current.val)
            print(p)

