from unittest import TestCase, main
from algoritmos.stack import Node, Stack

lista = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

class AlgoTests(TestCase):
    def test_node(self):
        n = Node(2)
        n.next = Node(3)
        self.assertEqual(n.value, 2)
        self.assertEqual(n.next.value, 3)

    def test_stack_push(self):
        s = Stack()
        for i, n in enumerate(lista):
            with self.subTest(i=i):
                self.assertEqual(s.push(n), i+1)

    def test_stack_pop(self):
        s = Stack()
        for n in lista:
            s.push(n)
        for i in range(len(lista)-1, -1, -1):
            with self.subTest():
                self.assertEqual(s.pop(), lista[i])

if __name__ == "__main__":
    main()