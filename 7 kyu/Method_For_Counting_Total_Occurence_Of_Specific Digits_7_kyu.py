# https://www.codewars.com/kata/56311e4fdd811616810000ce/train/python

# class List(object):
#     def count_spec_digits(self, integers_list, digits_list):

#         for digit in digits_list:
#             if not (0 <= digit <= 9):
#                 raise ValueError(f"Недопустимая цифра {digit}. Цифры должны быть от 0 до 9.")

#         frequency = {digit: 0 for digit in digits_list}
#         for number in integers_list:
#             number_str = str(abs(number))
#             for char in number_str:
#                 current_digit = int(char)
#                 if current_digit in frequency:
#                     frequency[current_digit] += 1
#         result = [(digit, frequency[digit]) for digit in digits_list]
        
#         return result



from collections import Counter


class List(object):
    @staticmethod
    def count_spec_digits(integers_list, digits_list):
        counts = Counter(''.join(str(abs(a)) for a in integers_list))
        return [(b, counts[str(b)]) for b in digits_list]
