class Queue:
    def __init__(self) -> None:
        self.queue = list()

    def __str__(self) -> str:
        str_items = ""
        for i in range(len(self.queue)):
            value = self.queue[i]
            str_items += str(value)
            if i + 1 < len(self.queue):
                str_items += ", "
        return f"Queue( {str_items} )"

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)


if __name__ == "__main__":
    elements = ["Milkshake", "Batata Frita", "Refrigerante"]
    content_queue = Queue()

    for elem in elements:
        content_queue.enqueue(elem)
    
    print(content_queue)

    content_queue.dequeue()

    print(content_queue)
