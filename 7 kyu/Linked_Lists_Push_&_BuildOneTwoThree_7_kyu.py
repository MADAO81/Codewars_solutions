# https://www.codewars.com/kata/55be95786abade3c71000079/train/python

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def push(head, data):
#     node_ = Node(data)
#     node_.next = head
#     return node_


# def build_one_two_three():
#     node_ = None
#     for i in [3, 2, 1]:
#         node_ = push(node_, i)
#     return node_



class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def push(head, data):
    return Node(data, head)
  
def build_one_two_three():
    return Node(1, Node(2, Node(3)))
