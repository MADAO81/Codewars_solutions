# Training JS #18: Methods of String object--concat() split() and its good friend join()

def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())
