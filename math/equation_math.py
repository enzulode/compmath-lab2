from equation.abstraction import EquationOne
from typing import *

def bisection_method(a: float, b: float, eq: EquationOne, eps: float = 0.01) -> float:
  x: float = (a + b) / 2
  funcA: float
  funcX: float
  while (abs(eq.func(x)) > eps):
    funcA = eq.func(a)
    funcX = eq.func(x)

    if (funcA * funcX > 0):
      a = x
    else:
      b = x
    
    x = (a + b) / 2
  
  return x

def newton_method(a: float, b: float, eq: EquationOne, eps: float = 0.01) -> float:
  if (not validate__left_border_less_than_right(a, b)):
    raise Exception('Invalid interval: left border should be less than right')

  if (not validate__single_root(a, b, eq)):
    raise Exception('Invalid interval: the requirement about singe root in the interval was not fullfilled')

  x: float
  if (eq.func(a) * eq.ddfunc(a) > 0):
    x = a
  elif (eq.func(b) * eq.ddfunc(b) > 0):
    x = b
  else:
    raise Exception('Calculation error. The method does not converge')
  
  n = 0
  while (abs(eq.func(x)) > eps):
    n += 1
    x -= eq.func(x) / eq.dfunc(x)
  
  return x, n

def basic_iterative_method(a: float, b: float, eq: EquationOne, eps: float = 0.01) -> float:
  if (not validate__left_border_less_than_right(a, b)):
    raise Exception('Invalid interval: left border should be less than right')

  if (not validate__single_root(a, b, eq)):
    raise Exception('Invalid interval: the requirement about singe root in the interval was not fullfilled')
  
  lmbda = -1 / max(eq.dfunc(a), eq.dfunc(b))
  n = 0
  x = a if eq.dfunc(a) > eq.dfunc(b) else b
  q = max(abs(1 + lmbda * eq.dfunc(a)), abs(1 + lmbda * eq.dfunc(b)))
  if (q > 1):
    raise Exception(f'There is no convergence on this interval, q = {q}')

  while(abs(eq.func(x)) > eps):
    n += 1
    x += lmbda * eq.func(x)

  return x, n

def validate__left_border_less_than_right(a: float, b: float) -> bool:
  return a < b

def validate__single_root(a: float, b: float, eq: EquationOne) -> bool:
  return eq.func(a) * eq.func(b) < 0


