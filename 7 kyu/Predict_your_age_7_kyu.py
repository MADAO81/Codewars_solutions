# Predict your age
# My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

# In honor of my grandfather's memory we will write a function using his formula!

# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.
# Example
# predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86



# import numpy as np
# def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
#     return np.sum(np.array([age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]) ** 2) ** 0.5 // 2


# def predict_age(*ages):
#     return sum(a*a for a in ages)**.5//2


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return ((age_1**2+age_2**2+ age_3**2+ age_4**2+ age_5**2+age_6**2+ age_7**2+age_8**2)**0.5)//2
