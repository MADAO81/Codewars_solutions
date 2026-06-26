# https://www.codewars.com/kata/5b609ebc8f47bd595e000627/train/python

# def solution(arr_val, arr_unit) :
#     G = 6.67e-11
#     conversion = {'kg': 1, 'g': 1e-3, 'mg': 1e-6, 'μg': 1e-9, 'lb': .453592,
#                   'm': 1, 'cm': 1e-2, 'mm': 1e-3, 'μm': 1e-6, 'ft': .3048}
#     m1, m2, d = arr_val
#     um1, um2, ud = arr_unit
#     return G * m1 * conversion[um1] * m2 * conversion[um2] / (d * conversion[ud]) ** 2

units = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
         "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048,
         "G": 6.67e-11}

def solution(v, u):
    m1, m2, r = (v[i] * units[u[i]] for i in range(3))
    return units["G"] * m1 * m2 / r**2
