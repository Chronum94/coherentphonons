import numpy as np
from coherentphonons.splines import PotentialFunctions, make_eps_splines_1d
from typing import Callable


def make_propagator_1d(*, potential_functions: PotentialFunctions, 
                       mass: float, 
                       damping: float = 0.0,
                       forcing_function: Callable = lambda t, y: 0.0,
                      ):
    def propagate_1d(t, y):
        dy = np.zeros_like(y)
        dy[0] = y[1]
        dy[1] = (potential_functions.f(y[0]) + forcing_function(t, y)) / mass - damping * y[1]
        return dy
    return propagate_1d
