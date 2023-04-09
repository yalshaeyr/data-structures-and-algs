# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:44:49 2023

@author: Yazen
"""

# The base unit in a linked list
# stores some data and a link to the next unit
class Node:
    def __init__(self, data, next = None):
        self.data = data

# Builds the linked list based on some data
# returns the head of the list
def build_llist(*data):
    # if there is no data, do not build a list
    if not len(data):
        return None 
    # otherwise, build the list
    else:
        # the head should have the first data point
        head = Node(data[0])
        # start building the rest of the list
        curr = head 
        for i in range(1, len(data)):
            # for each element, create a new node
            # and link it to the previous node
            new = Node(data[i])
            curr.next = new
            curr = new 
        curr.next = None 
        return head 
    
# prints the elements of the linked list
def print_llist(llist):
    while llist != None:
        print(llist.data, end = ' ')
        llist = llist.next 
    print()
    
# removes any duplicates from the linked list
# and returns the head
def removeDuplicates(llist):
    # keep a reference to the head and previous element
    head, prev = llist, llist  
    # keep track of what elements have been duplicated
    found = [llist.data]
    
    # while not at the end
    while llist != None:
        # if the element is not duplicated, keep it
        if llist.data not in found:
            prev.next = llist
            prev = llist 
            found.append(llist.data)
        # otherwise, skip it 
        llist = llist.next 
    prev.next = None 
            
    
    return head 
