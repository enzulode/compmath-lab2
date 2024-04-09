from typing import *
from math import *

from equation.abstraction import SystemTwo

def newton_method_systems(initial_approx: Tuple[float, float], system: SystemTwo, eps: float = 0.01) -> Tuple[float, float, int]:
  x: float = initial_approx[0]
  y: float = initial_approx[1]

  for i in range(10000):
    f1: float = system.get_equation1().func(x, y)
    f2: float = system.get_equation2().func(x, y)
    J: Tuple[Tuple[float, float], Tuple[float, float]] = system.get_jacobian(x, y)

    delta_x = (-f1 * J[1][1] + f2 * J[0][1]) / (J[0][0] * J[1][1] - J[0][1] * J[1][0])
    delta_y = (f1 * J[1][0] - f2 * J[0][0]) / (J[0][0] * J[1][1] - J[0][1] * J[1][0])

    x += delta_x
    y += delta_y

    if (abs(delta_x) < eps and abs(delta_y) < eps):
      return (x, y, i)
  
  raise Exception('Max ireation exceed. Computation errored: invalid data')
