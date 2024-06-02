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
  twos_comp_b = TWOS_COMP(b)
  sum, carry = FullAdder(a, twos_comp_b)
  borrow = ONES_COMP(carry)
  if borrow == '0':
    return '+'+sum
  return '-'+TWOS_COMP(sum)


  
