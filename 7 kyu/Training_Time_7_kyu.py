# https://www.codewars.com/kata/572ab0cfa3af384df7000ff8/train/python

# def shuffle_it(arr, *pairs):
#     result = arr.copy()
#     for i, j in pairs:
#         result[i], result[j] = result[j], result[i]
#     return result


def shuffle_it(arr,*time):
    for x,y in time:
        arr[x],arr[y]=arr[y],arr[x]
    return arr
