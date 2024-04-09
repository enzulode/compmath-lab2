from equation.abstraction import EquationOne

class ThirdEquation(EquationOne):
  def func(self, x: float) -> float:
    return x**3 + 2.28 * x**2 - 7.35 * x - 3.904

  def dfunc(self, x: float) -> float:
    return 3 * x**2 + 4.56 * x - 7.35

  def ddfunc(self, x: float) -> float:
    return 6 * x + 4.56
  
  def __str__(self) -> str:
    return "x^3 + 2.28x^2 - 7.35x - 3.904 = 0"
