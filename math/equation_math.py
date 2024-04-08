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

def newton_method(x0: float, eq: EquationOne, eps: float = 0.01) -> float:
  x: float = x0 - eq.func(x0) / eq.dfunc(x0)
  x0 = x

  while (abs(eq.func(x)) > eps):
    x = x0 - eq.func(x0) / eq.dfunc(x0)
    x0 = x
  
  return x

def basic_iterative_method(a: float, b: float, eq: EquationOne, eps: float = 0.01) -> float:
  derivative_a: float = eq.dfunc(a)
  derivative_b: float = eq.dfunc(b)
  lambd: float = -1 / max(derivative_a, derivative_b)
  x: float = a if derivative_a > derivative_b else b
  
  # covergence check

  while(abs(eq.func(x)) > eps):
    x += lambd * eq.func(x)

  return x