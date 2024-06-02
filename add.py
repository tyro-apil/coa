#!/usr/bin/env python3

"""add.py - Addition of two unsigned integer using binary number"""

"""Logic:
Using the boolean expression obtained from K-map

S = EX_OR(EX_OR(a,b),c)
C = OR(AND(a,b), AND(c, EX_OR(a,b)))
"""

from utils import FullAdder

def main():
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")

  sum, carry = FullAdder(num1, num2)

  print(f"{num1} + {num2} = sum:{sum} carry:{carry}")

if __name__=="__main__":
  main()