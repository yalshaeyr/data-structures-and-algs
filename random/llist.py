# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:44:49 2023

@author: Yazen
"""

class Node:
    def __init__(self, data, next = None):
        self.data = data

def build_llist(*data):
    if not len(data):
        return None 
    else:
        head = Node(data[0])
        curr = head 
        for i in range(1, len(data)):
            new = Node(data[i])
            curr.next = new
            curr = new 
        curr.next = None 
        return head 

def print_llist(llist):
    while llist != None:
        print(llist.data, end = ' ')
        llist = llist.next 
    print()

def removeDuplicates(llist):
    head, prev = llist, llist  
    found = [llist.data]
    
    while llist != None:
        if llist.data not in found:
            prev.next = llist
            prev = llist 
            found.append(llist.data)
        llist = llist.next 
    prev.next = None 
            
    
    return head 