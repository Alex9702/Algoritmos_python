from unittest import TestCase, main
from algoritmos.stack import Node

class AlgoTests(TestCase):
    def test_node(self):
        n = Node(2)
        n.next = 3
        self.assertEqual(n.value, 2)
        self.assertEqual(n.next.value, 3)

if __name__ == "__main__":
    main()