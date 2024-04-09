from typing import *
from math import *

from equation.abstraction import EquationTwo
from equation.abstraction import SystemTwo

class SystemEquation1(EquationTwo):
  def func(self, x: float, y: float) -> float:
    return sin(x) + 2*y - 2
  
  def dfunc_x(self, x: float, y: float) -> float:
    return cos(x)
  
  def dfunc_y(self, x: float, y: float) -> float:
    return 2
  
  def func_sided(self, x: float, y: float) -> float:
    return 1 - 0.5 * sin(x)
  
  def __str__(self) -> str:
    return 'sin(x) + 2y = 2'
  
class SystemEquation2(EquationTwo):
  def func(self, x: float, y: float) -> float:
    return x + cos(y - 1) - 0.7
  
  def dfunc_x(self, x: float, y: float) -> float:
    return 1
  
  def dfunc_y(self, x: float, y: float) -> float:
    return -sin(y - 1)
  
  def func_sided(self, x: float, y: float) -> float:
    return 0.7 - cos(y - 1)

  def __str__(self) -> str:
    return 'x + cos(y - 1) = 0.7'
  
class SecondSystem(SystemTwo):
  def __init__(self) -> None:
    super().__init__()
    self.__eq1: EquationTwo = SystemEquation1()
    self.__eq2: EquationTwo = SystemEquation2()

  def get_equation1(self) -> EquationTwo:
    return self.__eq1
  
  def get_equation2(self) -> EquationTwo:
    return self.__eq2