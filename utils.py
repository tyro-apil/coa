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
