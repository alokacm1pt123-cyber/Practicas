class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)