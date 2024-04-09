from typing import *
from equation.abstraction import EquationTwo

from math import *


class FirstSystemEquation1(EquationTwo):
  def func(self, x: float, y: float) -> float:
    return tan(x*y + 0.1) - x*x
  
  def dfunc_x(self, x: float, y: float) -> float:
    return (1 / cos(x * y + 0.1) ** 2) * y - 2 * x
  
  def dfunc_y(self, x: float, y: float) -> float:
    return (1 / cos(x * y + 0.1) ** 2) * x
  
  def __str__(self) -> str:
    return 'tg(xy + 0.1) = x^2'
  
class FirstSystemEquation2(EquationTwo):
  def func(self, x: float, y: float) -> float:
    return x ** 2 + 2 * y ** 2 - 1
  
  def dfunc_x(self, x: float, y: float) -> float:
    return 2 * x
  
  def dfunc_y(self, x: float, y: float) -> float:
    return 4 * y

  def __str__(self) -> str:
    return 'x^2 + 2y^2 = 1'