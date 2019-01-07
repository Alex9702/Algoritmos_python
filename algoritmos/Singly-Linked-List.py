class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class SimpleLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
            self.length = 1
            return self

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        self.tail = node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        if not self.head.next:
            self.head = self.tail = None
            self.length = 0
            return None

        current = self.head

        while current.next:
            newTail = current
            current = current.next
        newTail.next = None
        self.tail = newTail
        self.length -= 1
        return self
    
    def shift(self):
        if not self.head:
            return None
        self.head = self.head.next
        self.length -= 1
        return self

    def unshift(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def get(self, index):
        if index > self.length or index < 0:
            return None
        currentIdx = 0
        current = self.head
        while current:
            if index == currentIdx:
                return current
            current = current.next
            currentIdx += 1

    def set(self, index, value):
        if self.length < index or index < 0:
            return None
        current = self.head
        currentIdx = 0
        while current:
            if currentIdx == index:
                current.value = value
            current = current.next
            currentIdx += 1            

    def include(self, index, value):
        if 0 > index or index > self.length:
            return None
        current = self.head
        currentIdx = 0
        while current.next:
            if index == currentIdx:
                node = Node(value)
                node.next = current
                current.next = node
                self.length += 1
                return self
            current = current.next
            currentIdx += 1

        return current.push(value)



    def list(self):
        l = []
        if self.head:
            current = self.head
            while current:
                l.append(current.value)
                current = current.next
        return l

lista = SimpleLinkedList()
lista.push(22)
lista.push(2)
lista.push(77)
lista.push(6)
lista.push(43)
lista.push(76)
lista.include(2,44)
print(lista.list())
print(lista.length)