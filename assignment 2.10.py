class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # push the element onto the first stack
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            # if the second stack is empty, pop all elements from the first stack
            # and push them onto the second stack
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            # if both stacks are empty, return None
            return None

        # pop the top element from the second stack and return it
        return self.stack2.pop()
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # output: 1
print(queue.dequeue())  # output: 2
queue.enqueue(4)
print(queue.dequeue())  # output: 3
print(queue.dequeue())  # output: 4
print(queue.dequeue())  # output: None
