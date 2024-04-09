from typing import *
from math import *

from equation.abstraction import EquationTwo
from equation.abstraction import SystemTwo

class SystemEquation1(EquationTwo):
  def func(self, x: float, y: float) -> float:
    return sin(x + 1) - y - 1.2
  
  def dfunc_x(self, x: float, y: float) -> float:
    return cos(x + 1)
  
  def dfunc_y(self, x: float, y: float) -> float:
    return -1
  
  def __str__(self) -> str:
    return 'sin(x + 1) - y = 1.2'
  
class SystemEquation2(EquationTwo):
  def func(self, x: float, y: float) -> float:
    return 2 * x + cos(y) - 2
  
  def dfunc_x(self, x: float, y: float) -> float:
    return 2
  
  def dfunc_y(self, x: float, y: float) -> float:
    return -sin(y)

  def __str__(self) -> str:
    return '2x + cos(y) = 2'
  
class FirstSystem(SystemTwo):
  def __init__(self) -> None:
    super().__init__()
    self.__eq1: EquationTwo = SystemEquation1()
    self.__eq2: EquationTwo = SystemEquation2()

  def get_equation1(self) -> EquationTwo:
    return self.__eq1
  
  def get_equation2(self) -> EquationTwo:
    return self.__eq2
