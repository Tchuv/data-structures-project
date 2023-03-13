"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack, Node


class Tets_Stack_Node(unittest.TestCase):
    def test_nod(self):
        n1 = Node(11, None)
        n2 = Node('c', n1)
        self.assertEqual((n1.data), 11)
        self.assertEqual((n2.data), "c")

    def test_stack(self):
        stack = Stack()
        stack.push('Kolia')
        stack.push('Tolia')
        stack.push('Olia')
        self.assertEqual((stack.top.data), "Olia")
        self.assertEqual((stack.top.next_node.next_node.data), "Kolia")


if __name__ == '__main__':
    unittest.main()
