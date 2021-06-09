# Queue is a Linear Datastructure in which data is organized like a queue.
# The queue is operating in FIFO manner.
# Adding an element to queue is called Enqueue
# Removing an element from a queue called Dequeue

class Queue:
    def __init__(self) -> None:
        self.queue = list()
        self.first = -1
        self.last  = -1
        
    #Enqueue - Add new element at the end of queue
    def enqueue(self, value):
        if self.first == -1:
            self.first += 1
        self.last += 1
        self.queue.insert(self.last, value)
    
    def print(self):
        print(self.queue[self.first:self.last+1])

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print()