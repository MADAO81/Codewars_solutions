# Moving Zeros To The End
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]



# def move_zeros(lst):
#     temporary_list = []
#     new_lst = []
#     for i in lst:
#         if i == 0 :
#             temporary_list.append(0)
#         else:
#             new_lst.append(i)
    
#     return new_lst + temporary_list



def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array
