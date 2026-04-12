# https://www.codewars.com/kata/5434283682b0fdb0420000e6/train/python
def caffeine_buzz(n):
    if n % 12 == 0:
      return "CoffeeScript"
    if n % 6 == 0:
      return "JavaScript"
    if n % 3 == 0:
      return "Java"
    else:
      return "mocha_missing!"
