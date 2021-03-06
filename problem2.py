# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

import array as arr

def main():
  print(even_fib_sum(100))
  print(even_fib_sum(4000000))

def even_fib_sum(limit):
  if(limit < 2):
    return 0
  elif(limit == 2):
    return 2
  even_sum = 2
  first_term = 1
  second_term = 2
  new_term = 3
  while(new_term <= limit):
    first_term = second_term
    second_term = new_term
    if((new_term % 2) == 0):
      even_sum = even_sum + new_term
    new_term = first_term + second_term
  return even_sum

main()
