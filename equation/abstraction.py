from abc import ABC, abstractmethod
from typing import *

# Equation abstraction with single unknown variable
class EquationOne(ABC):
  # This method represents function
  @abstractmethod
  def func(self, x: float) -> float:
    raise Exception('Not implemented yet')

  # This method represents function derivative
  @abstractmethod
  def dfunc(self, x: float) -> float:
    raise Exception('Not implemented yet')
  
  # This method represenets second function derivative
  @abstractmethod
  def ddfunc(self, x: float) -> float:
    raise Exception('Not implemented yet')
  
  # This methid is responsible for the string representation of the equation
  @abstractmethod
  def __str__(self) -> str:
    raise Exception('Not implemented yet')


# Equation abstraction with two unknown variables
class EquationTwo(ABC):
  # This method represents function
  @abstractmethod
  def func(self, x: float, y: float) -> float:
    raise Exception('Not implemented yet')
  
  # This method represents function derivative by x
  @abstractmethod
  def dfunc_x(self, x: float, y: float) -> float:
    raise Exception('Not implemented yet')
  
  # This method represents function derivative by y
  @abstractmethod
  def dfunc_y(self, x: float, y: float) -> float:
    raise Exception('Not implemented yet')
  
  # This methid is responsible for the string representation of the equation
  @abstractmethod
  def __str__(self) -> str:
    raise Exception('Not implemented yet')

class SystemTwo(ABC):
  # First system equation getter
  @abstractmethod
  def get_equation1(self) -> EquationTwo:
    raise Exception('Not implemented yet')
  
  # Second system equation getter
  @abstractmethod
  def get_equation2(self) -> EquationTwo:
    raise Exception('Not implemented yet')

  # Calculates jacobian for the specific x and y values
  def get_jacobian(self, x: float, y: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    first_part: Tuple[float, float] = (self.get_equation1().dfunc_x(x, y), self.get_equation1().dfunc_y(x, y))
    second_part: Tuple[float, float] = (self.get_equation2().dfunc_x(x, y), self.get_equation2().dfunc_y(x, y))
    return (first_part, second_part)
