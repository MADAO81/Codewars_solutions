# https://www.codewars.com/kata/54d472e98776e4eb5b000215/train/python

# def pitch_class(note: str) -> int | None:
#         base_values = {
#         'C': 0,
#         'D': 2,
#         'E': 4,
#         'F': 5,
#         'G': 7,
#         'A': 9,
#         'B': 11
#         }
#         if not note or len(note)==0:
#             return None
#         letter = note[0].upper()
#         if  letter not in base_values:
#             return None
#         value = base_values[letter]
#         for modifier in note[1:]:
#             if modifier == "#":
#                 value +=1
#             elif modifier == "b":
#                 value -= 1
#             else:
#                 return None
#         value %= 12
#         return value


def pitch_class(str):
    value = {"C": 0, "D":2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    if value.get(str[0]) != None:
        if len(str) == 2:
            if "#" in str:
                if str[0] == "B":
                    return 0
                else:
                    return value.get(str[0]) + 1
            elif "b" in str:
                if str[0] == "C":
                    return 11
                else:
                    return value.get(str[0]) - 1
            else:
                return None
        else:
            return value.get(str, None)
    else: 
        return None
    pass
