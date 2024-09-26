class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == '__main__':
    # Example usage
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.peek())  # Output: 20
    s.pop()

    # Example usage
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
