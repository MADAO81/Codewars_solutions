# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python

def row_weights(array):
    team_one = array[::2]
    team_two = array[1::2]
    return sum(team_one),sum(team_two)
    
