import numpy as np
from coherentphonons.pes import PotentialFunctions


def make_propagator_1d(potential_functions: PotentialFunctions, mass: float, damping: float):
    def propagate_1d(t, y):
        dy = np.zeros_like(y)
        dy[0] = y[1]
        dy[1] = potential_functions.f(y[0]) * y[0] / mass #- damping * y[1]
        return dy
    return propagate_1d
