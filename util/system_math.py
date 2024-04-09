from typing import *
from math import *

from equation.abstraction import EquationTwo

def jacobian(x: float, y: float, eq1: EquationTwo, eq2: EquationTwo):
  return ((eq1.dfunc_x(x, y), eq1.dfunc_y(x, y)), (eq2.dfunc_x(x, y), eq2.dfunc_y(x, y)))

def newton_method_systems(initial_approx: Tuple[float, float], eq1: EquationTwo, eq2: EquationTwo, eps: float = 0.01) -> Tuple[float, float, int]:
  x: float = initial_approx[0]
  y: float = initial_approx[1]

  for i in range(10000):
    f1: float = eq1.func(x, y)
    f2: float = eq2.func(x, y)
    J: Tuple[Tuple[float, float], Tuple[float, float]] = jacobian(x, y, eq1, eq2)

    delta_x = (-f1 * J[1][1] + f2 * J[0][1]) / (J[0][0] * J[1][1] - J[0][1] * J[1][0])
    delta_y = (f1 * J[1][0] - f2 * J[0][0]) / (J[0][0] * J[1][1] - J[0][1] * J[1][0])

    x += delta_x
    y += delta_y

    if (abs(delta_x) < eps and abs(delta_y) < eps):
      return (x, y, i)
  
  raise Exception('Max ireation exceed. Computation errored: invalid data')
