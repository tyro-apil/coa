"""utils.py - Utilities"""

def NOT(ch):
  if ch=='0':
    return '1'
  return '0'

def OR(a,b):
  if a=='1' or b=='1':
    return '1'
  return '0'

def AND(a,b):
  if a=='0' or b=='0':
    return '0'
  return '1'

def EX_OR(a,b):
  if a==b:
    return '0'
  return '1'

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
