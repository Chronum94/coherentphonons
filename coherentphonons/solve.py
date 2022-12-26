from scipy.integrate import solve_ivp
from typing import Callable


def solve(propagator: Callable, t_span, y0):
    sol = solve_ivp(propagator, t_span, y0, dense_output=True)
    return sol
