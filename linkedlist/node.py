class Node:
    def __init__(self, value) -> None:
        self.prev = None
        self.value = value
        self.next = None

    def __str__(self) -> str:
        prev_value = self.prev.value if self.prev else None
        next_value = self.next.value if self.next else None
        return f"prev(Node={prev_value}), NODE(Value={self.value}), next(Node={next_value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def __str__(self) -> str:
        node = self.head
        node_list = []
        if node is None:
            return "empty"
        while node:
            node_list.append(f"{node}")
            node = node.next
        return f"Length={self.__length} " + " -> ".join(node_list)

    def __len__(self):
        return self.__length

    def __get_node_at(self, position):
        pointer = self.head
        while position > 0:
            pointer = pointer.next
            position -= 1
        return pointer

    def insert_first(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node

        if not self.head:
            self.head = node
            self.tail = node

        self.__length += 1

    def insert_last(self, value):
        node = Node(value)

        if self.head:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        if self.head is None:
            self.head = node
            self.tail = node
        self.__length += 1

    def get_element_at(self, position):
        value_returned = None
        pointer = self.head
        if pointer:
            pointer = self.__get_node_at(position)
        if pointer:
            value_returned = pointer.value
        return value_returned

    def set_element_at(self, position, element):
        node = Node(element)
        value_returned = None
        pointer = self.head
        if pointer:
            while position > 0 and pointer.next:
                pointer = pointer.next
                position -= 1
        if pointer:
            pointer.value = node.value
            value_returned = pointer.value
        return value_returned

    def insert_at(self, position, element):
        node = Node(element)
        value_returned = None
        pointer = self.head
        if not self.head:
            return self.insert_first(element)

        pointer = self.__get_node_at(position)
        if pointer:
            pointer.prev.next = node
            pointer.next.prev = node
            node.next = pointer.next
            node.prev = pointer.prev
        if not pointer:
            return self.insert_last(element)
        self.__length += 1

        return value_returned

    def remove_first(self):
        if self.head is None:
            return self.is_empty()
        pointer = self.head
        if self.head:
            self.head = pointer.next
            pointer.prev = None

        self.__length -= 1
        return pointer

    def remove_last(self):
        pointer = self.head
        while pointer.next:
            previus_node = pointer
            pointer = pointer.next
        previus_node.next = None
        self.tail = previus_node
        self.__length -= 1

    def remove_at(self, position):
        pointer = self.head
        if position == 0:
            return self.remove_first()
        if pointer.next is None:
            return self.remove_last()
        pointer = self.__get_node_at(position)
        self.__length -= 1
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev

    def index_of(self, value):
        pointer = self.head
        position = 0
        while pointer:
            if pointer.value == value:
                return position
            position += 1
            pointer = pointer.next
        return -1

    def is_empty(self):
        return not self.__length

    def clear(self):
        while not self.is_empty():
            self.remove_first()
    
    def remove_duplicate(self, linkdList):
        if len(linkdList) < 1:
            return linkdList
        current_element = linkdList.head
        while current_element and current_element.next:
            if current_element.value == current_element.next.value:
                current_element.next = current_element.next.next
            else:
                current_element = current_element.next
        print(linkdList)
        return linkdList
    
    def remove_duplicate_doubleList(self, linkdList):
        if len(linkdList) < 1:
            return linkdList
        filterd_list = LinkedList()
        while linked_list:
            current_node = linkdList.remove_first()
            if linkdList.index_of(current_node.value) == -1:
                filterd_list.insert_last(current_node.value)
        print(filterd_list)
        return filterd_list

linked_list = LinkedList()

linked_list.insert_first(1)
linked_list.insert_first(2)
linked_list.insert_first(2)
linked_list.insert_first(2)
linked_list.insert_first(3)
linked_list.insert_first(3)
linked_list.insert_first(3)

linked_list.remove_duplicate_doubleList(linked_list)
""" 


linked_list.clear()
print(linked_list.is_empty())
linked_list.insert_last(1)
print("------")
linked_list = LinkedList()
linked_list.insert_last(2)
print("------")
linked_list.insert_last(3)
print("------")
print(linked_list.get_element_at(0))
linked_list.set_element_at(0, 3)
print(linked_list.get_element_at(0))
print("------")
linked_list.insert_first(1)
print(linked_list)
print("------")
print(linked_list.get_element_at(0))
linked_list.insert_at(1, 10)
print(linked_list)
print("------")
linked_list.remove_first()
print(linked_list)
print("------")
linked_list.insert_last(4)
print(linked_list)
print("------")
linked_list.remove_last()
print(linked_list)
print(linked_list.get_element_at(1))
print("------")
linked_list.remove_at(1)
print(linked_list)  """
