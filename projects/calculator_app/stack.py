class ArrayStack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("상태: 스택 포화(Stack Overflow)")

    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        return None

    def isFull(self):
        return self.top == self.capacity - 1

    def isEmpty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def clear(self):
        self.top = -1