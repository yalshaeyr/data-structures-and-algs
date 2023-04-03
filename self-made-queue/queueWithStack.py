#Represents an item in a stack or queue 
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val 
        self.next = None 
    def __str__(self):
        return f"{self.val}"

# A stack which follows LIFO 
class Stack(object):
    def __init__(self, first=None):
        self.first = None 
    # Add a node to the stack 
    def push(self, val):
        node = Node(val)
        node.next = self.first
        self.first = node 
    # Remove and return the top node 
    def pop(self):
        temp = self.first 
        self.first = self.first.next 
        return temp 
    # Return the top node 
    def top(self):
        return self.first
    # Check if there are any nodes in the stack 
    def empty(self):
        return self.first == None 
    # Print the stack 
    def print(self):
        temp = self.first 
        while temp != None:
            print(temp.val)
            temp = temp.next 

# A queue created from two stacks - follows FIFO 
class Queue(object):
    # Initialise the two stacks 
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    # Move one stack's contents to the other 
    # This way, the nodes' order is flipped 
    def moveOver(self, fro, to):
        while not fro.empty():
            to.push(fro.pop())
    # Push a node into the queue 
    def push(self, data):
        self.moveOver(self.s1, self.s2)
        self.s2.push(data)
        self.moveOver(self.s2, self.s1)
    # Pop and return the front node 
    def pop(self):
        return self.s1.pop()    
    # Return the front node 
    def front(self):
        return self.s1.top()
    # Print the queue 
    def printUnderlying(self):
        self.s1.print()

# Simple test function 
if __name__== '__main__':
    # Open the test file 
    with open("test.txt") as testFile:
        n = int(testFile.readline())        
        myQueue = Queue() # Declare the queue
        # Loop through each command 
        for i in range(n):
            vals = list(map(int, testFile.readline().split()))
            # Push a value 
            if len(vals) > 1:
                myQueue.push(vals[1])
            # Remove a value  
            elif vals[0] == 2:
                myQueue.pop()
            # Print the queue 
            elif vals[0] == 3:
                print(myQueue.front())
