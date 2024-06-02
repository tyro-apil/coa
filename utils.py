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
  num1, num2 = add_zero_padding(num1, num2)
  num1, num2 = num1[::-1], num2[::-1]
  for bit1, bit2 in zip(num1, num2):
    sum += EX_OR(EX_OR(bit1, bit2),carry)
    carry = OR(AND(bit1, bit2), AND(carry, EX_OR(bit1, bit2)))
  return sum[::-1], carry[::-1]

def add_zero_padding(num1: str, num2: str):
  max_len = max(len(num1), len(num2))

  num1 = num1.zfill(max_len)
  num2 = num2.zfill(max_len)

  return num1, num2

def ONES_COMP(a:str):
  ones_comp = ""
  for char in a:
    if char=='0':
      ones_comp += '1'
    else:
      ones_comp += '0'
  return ones_comp

def TWOS_COMP(a:str):
  ones_comp = ONES_COMP(a)
  sum, carry = FullAdder(ones_comp, '1')
  if carry != '0':
    return carry + sum
  return sum

def FullSubtractor(a: str, b: str):
  a,b = add_zero_padding(a,b)
  # a = '0'+a
  # b = '0'+b
  twos_comp_b = TWOS_COMP(b)
  sum, carry = FullAdder(a, twos_comp_b)
  borrow = ONES_COMP(carry)
  return borrow+sum

def Multiply(a: str, b: str):
  # Set partial sum=0, multipier and multiplicand
  partial_sum = '0'
  multiplicand = a
  multiplier = b

  # max_len, zero padding
  n = max(len(multiplicand), len(multiplier))
  multiplicand, multiplier = add_zero_padding(multiplicand, multiplier)
  reversed_multiplier = multiplier[::-1]

  # operate for max_len times
  for _ in range(n):
    carry = '0'
    if reversed_multiplier[0] == '1':
      partial_sum, carry = FullAdder(partial_sum, multiplicand)

    # Shift multiplier
    reversed_multiplier = reversed_multiplier[1:]+partial_sum[::-1][0]
    # Shift partial sum
    partial_sum = carry + partial_sum[:-1]

  return partial_sum + reversed_multiplier[::-1]

  
