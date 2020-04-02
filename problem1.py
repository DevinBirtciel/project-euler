# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
  naive(1000)
  functional_sum(1000)

def series_function(multiple, limit):
  n = (limit - 1) // multiple
  return multiple * (((n * n) + n) // 2)

def functional_sum(number):
  sum_3 = series_function(3, number)
  sum_5 = series_function(5, number)
  sum_15 = series_function(15, number)
  print(sum_3 + sum_5 - sum_15)

def naive(number):
  sum = 0
  counter = 0
  while counter < number:
    if multiple_3_or_5(counter) == True:
      sum += counter
    counter += 1
  print(sum)

def multiple_3_or_5(number):
  if(multiple(number, 3)):
    return True
  elif (multiple(number, 5)):
    return True
  else:
    return False

def multiple(number, multiple):
  return True if number % multiple == 0 else False

main()
