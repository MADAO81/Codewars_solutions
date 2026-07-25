# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

# Some cases:
# [22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

# [68, -1, 1, -7, 10, 10] => [-1, 10]

# [-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]



# def multiple_of_index(arr):
#     return [j for i,j in enumerate(arr) if (j==0 and i==0) or (i!=0 and j%i==0)]


# def multiple_of_index(arr):
#     #remainder = 0 , arr item / its index
#     x = []
#     for i in range(len(arr)):
        
#         if arr[i] == 0:
#             x.append(arr[i])
#             continue
        
#         if i == 0: continue
        
#         if (arr[i] % i) == 0:
#             x.append(arr[i])
#     return x



def multiple_of_index(arr):
    result = []
    if arr[0] == 0:
        result.append(0)
    for i in range(1,len(arr)):
        if arr[i] % i ==0:
            result.append(arr[i])
    return result

