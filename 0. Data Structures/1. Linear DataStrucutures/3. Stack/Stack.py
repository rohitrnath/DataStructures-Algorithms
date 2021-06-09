# Stack is a linear data structure in which data is organized in one top of another like a stack
# The Stack is operating in LIFO manner. Means last to enter stack should leave first from stack.
# Inserting a element to stack is called Push Operation
# Removing a element from a stack is called Pop Operation

class Stack:

    def __init__(self) -> None:
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if(len(self.stack) < 1):
            print("The Stack Is Empty!")
        else:
            self.stack.pop()

    def print(self):
        print(self.stack)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.print()

stack.pop()

stack.print()