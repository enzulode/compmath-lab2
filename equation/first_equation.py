from equation.abstraction import EquationOne

class FirstEquation(EquationOne):
  def func(self, x: float) -> float:
    return x ** 3 + 4 * x - 6

  def dfunc(self, x: float) -> float:
    return 3 * x**2 + 4

  def __str__(self) -> str:
    return "x^3 + 4x - 6 = 0"
