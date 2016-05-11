# MIT 6.189
# Homework 3 Ex 3.6 Your First Class
# Author: Hao Zhang
# Date: 2016.4.29
# File: queue.py

class Queue:
    def __init__(self):
        self.L = []

    def insert(self, n):
        self.L.append(n)

    def remove(self):
        if len(self.L) == 0:
            print 'The queue is empty'
        else:
            x = self.L.pop(0)
            print x

# Test
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()
