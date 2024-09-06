import unittest
from node import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_first(self):
        self.linked_list.insert_first(1)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 1)
        self.assertEqual(len(self.linked_list), 1)

    def test_insert_last(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(2)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 2)
        self.assertEqual(len(self.linked_list), 2)

    def test_insert_at(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(3)
        self.linked_list.insert_at(2, 1)
        self.assertEqual(self.linked_list.head.next.value, 3)
        self.assertEqual(len(self.linked_list), 3)

    def test_remove_first(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(2)
        self.linked_list.remove_first()
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(len(self.linked_list), 1)

    def test_remove_last(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(2)
        self.linked_list.remove_last()
        self.assertEqual(self.linked_list.tail.value, 1)
        self.assertEqual(len(self.linked_list), 1)

    def test_remove_at(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(2)
        self.linked_list.insert_last(3)
        self.linked_list.remove_at(1)
        self.assertEqual(self.linked_list.head.next.value, 3)
        self.assertEqual(len(self.linked_list), 2)

    def test_get_element_at(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(2)
        element = self.linked_list.get_element_at(1)
        self.assertEqual(element, 2)

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.linked_list.insert_last(1)
        self.assertFalse(self.linked_list.is_empty())
    
    def test_clear(self):
        self.linked_list.insert_first(1)
        self.linked_list.insert_first(2)
        self.linked_list.insert_first(3)
        self.linked_list.clear()
        self.assertTrue(self.linked_list.is_empty())

    def test_index_of(self):
        self.linked_list.insert_last(1)
        self.linked_list.insert_last(2)
        self.linked_list.insert_last(3)
        self.assertEqual(self.linked_list.index_of(2), 1)
        self.assertEqual(self.linked_list.index_of(3), 2)
        self.assertEqual(self.linked_list.index_of(4), -1)



if __name__ == "__main__":
    unittest.main()
