# https://www.codewars.com/kata/59fa8e2646d8433ee200003f/train/python


# def sort_by_bit(arr): 
#     arr.sort(key=lambda n: (n.bit_count(),n))



def sort_by_bit(arr):
    arr.sort(key=lambda x:(bin(x).count('1'), x))   # they wanted to modify the input

    return arr
