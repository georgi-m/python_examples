###
### A simple stack class with basic stack funtionalities.
###
### 1) push() - To put an object on the top of the stack. 
### 2) pop() - To remove and return the top element.
### 3) isEmpty() - method returns true if nothing is on the stack.
### 4) isFull() - method returns true if stack is full.

import config

class Stack:
     size = 1
     def __init__(self):
         self.items = []

     def push(self, item):
         if self.isFull():
                config.log_example.warning('Stack is full')
         else:
                self.items.append(item)

     def pop(self):
         if self.isEmpty():
                config.log_example.warning('Stack is empty')
         else:
                return self.items.pop()

     def isEmpty(self):
         return self.items == []

     def isFull(self):
         return len(self.items) == self.size

     def size(self):
         return len(self.items)

     def print_all(self):
         print self.items
