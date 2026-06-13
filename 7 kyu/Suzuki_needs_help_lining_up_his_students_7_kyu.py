# https://www.codewars.com/kata/5701800886306a876a001031/train/python

# def lineup_students(st):
#     names = st.split()
#     return sorted(names, key = lambda x:(len(x),x), reverse=True)


def lineup_students(st):
    return sorted(st.split(), key=lambda x:(len(x),x), reverse=True)
