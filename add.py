#!/usr/bin/env python3

"""add.py - Addition of two unsigned integer using binary number"""

"""Logic:
Using the boolean expression obtained from K-map

S = EX_OR(EX_OR(a,b),c)
C = OR(AND(a,b), AND(c, EX_OR(a,b)))
"""

from utils import NOT, AND, OR, EX_OR

def FullAdder(num1, num2):
  """
  Arguments: binary strings of equal length
  Returns: sum and carry as tuple
  """
  sum = ''
  carry = '0'
  for bit1, bit2 in zip(num1, num2):
    sum += EX_OR(EX_OR(bit1, bit2),carry)
    carry = OR(AND(bit1, bit2), AND(carry, EX_OR(bit1, bit2)))
  return sum, carry

def main():
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")

  max_len = max(len(num1), len(num2))

  # Padding zeroes infront 
  num1 = num1.zfill(max_len)
  num2 = num2.zfill(max_len)

  # Reverse the string
  num1 = num1[::-1]
  num2 = num2[::-1]

  sum, carry = FullAdder(num1, num2)
  sum = sum[::-1]
  print(f"{num1} + {num2} = sum:{sum} carry:{carry}")

if __name__=="__main__":
  main()