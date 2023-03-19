#Implement a queue using the stack data structure


class Stack:
    def __init__(self):
        self.items = []
    
    # check if the stack is empty
    def is_empty(self):
        return self.items == []
    
    # push an element onto the stack
    def push(self, item):
        self.items.append(item)
    
    # pop an element from the stack
    def pop(self):
        return self.items.pop()
    
    # peek the top element of the stack without removing it
    def peek(self):
        return self.items[-1]
    
    # get the size of the stack
    def size(self):
        return len(self.items)

# Define Queue class to represent a queue data structure
class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    # check if the queue is empty
    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()
    
    # add an element to the back of the queue
    def enqueue(self, item):
        self.in_stack.push(item)
    
    # remove the element at the front of the queue and return it
    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
    
    # get the size of the queue
    def size(self):
        return self.in_stack.size() + self.out_stack.size()

# test the program with a sample input
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
