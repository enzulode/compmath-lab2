from equation.abstraction import EquationOne
from math import exp

class SecondEquation(EquationOne):
  def func(self, x: float) -> float:
    return 3*x + exp(x) + 5

  def dfunc(self, x: float) -> float:
    return 3 + exp(x)
  
  def ddfunc(self, x: float) -> float:
    return exp(x)
  
  def __str__(self) -> str:
    return "3x + e^x + 5 = 0"
