# https://www.codewars.com/kata/529f32794a6db5d32a00071f/train/python

# class Calculator:
#     @staticmethod
#     def average(*args):
#         return 0 if not args else sum(args) / len(args)



# from statistics import mean

# class Calculator:
#     @staticmethod
#     def average(*args):
#         return mean(args or [0])




class Calculator:
    @staticmethod
    def average(*args):
        return sum(args)/len(args) if args else 0
