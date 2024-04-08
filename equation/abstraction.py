from abc import ABC, abstractmethod

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
  
  # This methid is responsible for the string representation of the equation
  @abstractmethod
  def __str__(self) -> str:
    raise Exception('Not implemented yet')


# Equation abstraction with two unknown variables
class EquationTwo(ABC):
  @abstractmethod
  def func(self, x: float, y: float) -> float:
    raise Exception('Not implemented yet')
