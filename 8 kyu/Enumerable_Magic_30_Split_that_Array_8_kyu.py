# Create a method partition that accepts a list and a method/block. 
# It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.

# Here's a simple Ruby example:

# animals = ["cat", "dog", "duck", "cow", "donkey"]
# partition(animals){|animal| animal.size == 3}
#     #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
# The equivalent in Python would be:

# animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
# partition(animals, lambda x: len(x) == 3)
#     # (['cat', 'dog', 'cow'], ['duck', 'donkey'])



# def partition(arr, classifier_method):
#     return ([x for x in arr if classifier_method(x)], [x for x in arr if not classifier_method(x)])
  

def partition(list, classifier_method):
    listTrue = []
    listFalse = []
    for l in list:
        if classifier_method(l):
            listTrue.append(l)
        else:
            listFalse.append(l)
    return listTrue, listFalse
