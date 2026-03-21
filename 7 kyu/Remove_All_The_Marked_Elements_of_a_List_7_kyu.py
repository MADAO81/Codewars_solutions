# Define a method/function that removes from a given array of integers all the values contained in a second array.

# Examples (input -> output):
# * [1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]
# * [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2] -> [5, 6, 7, 8]
# * [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3] -> [8, 7, 6, 5, 1]


# class List(object):
#     @staticmethod 
#     def remove_(integer_list, values_list):
#         values_list = set(values_list)
#         return [a for a in integer_list if a not in values_list]

class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]
