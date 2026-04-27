# https://www.codewars.com/kata/57f604a21bd4fe771b00009c/train/python

def meeting(rooms):
    if "O" not in rooms:
        return "None available!"
    else:
        return rooms.index("O")
