# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/python

# def to_csv_text(array):
#     csw_rows = []
#     for row in array:
#         csw_row = ",".join(str(num) for num in row)
#         csw_rows.append(csw_row)
#     return "\n".join(csw_rows)


def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)
