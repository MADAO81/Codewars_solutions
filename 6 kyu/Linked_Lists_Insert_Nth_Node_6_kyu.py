# https://www.codewars.com/kata/55cacc3039607536c6000081/train/python


# class Node(object):
#     def __init__(self, data, nxt = None):
#         self.data = data
#         self.next = nxt
    
# def insert_nth(head, index, data):
#   if index == 0: return Node(data, head)
#   if head and index > 0:
#     head.next = insert_nth(head.next, index - 1, data)
#     return head
#   raise ValueError




def insert_nth(head, index, data):
    if index < 0:
        raise ValueError("Index must be non-negative")
    
    if index == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    if head is None:
        raise ValueError("Index is too large")
    
    head.next = insert_nth(head.next, index - 1, data)
    return head
