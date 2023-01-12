from scipy.integrate import solve_ivp
from typing import Callable
from coherentphonons.units import time_in_ps


def solve(propagator: Callable, t_span, y0, **kwargs):
    t_span = tuple(map(lambda x: x / time_in_ps))
    sol = solve_ivp(propagator, t_span, y0, **kwargs)
    return sol
