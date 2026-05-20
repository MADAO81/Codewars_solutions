# https://www.codewars.com/kata/56548dad6dae7b8756000037/train/python

# def what_is_the_time(time_in_mirror):
#     hour = int(time_in_mirror[0:2])
#     minute = int(time_in_mirror[3:5])
    
#     if hour < 11:
#         hour1 = 11 - hour
#     else:
#         hour1 = 23 - hour
        
#     minute1 = 60 - minute
#     if minute1 == 60:
#         minute1 -= 60
#         hour1 += 1
#     if hour1 > 12:
#         hour1 -= 12
#     result = ''
#     if hour1 > 9:
#         result = str(hour1) + ':'
#     else:
#         result = '0' + str(hour1) + ':'
#     if minute1 > 9:
#         result += str(minute1)
#     else:
#         result += '0' + str(minute1)
#     return result


def what_is_the_time(time_in_mirror):
    h, m = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)
