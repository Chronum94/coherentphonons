from coherentphonons.splines import PotentialFunctions, make_eps_splines_1d
import numpy as np
from scipy.integrate import solve_ivp
import pytest


def test_propagation():
    pes = PotentialFunctions(lambda x: 0.5 * x ** 2, lambda x: -x, lambda x: 1.0)
    def propagate_1d(t, y):
        dy = np.zeros_like(y)
        dy[0] = y[1]
        dy[1] = pes.f(y[0])
        return dy

    sol = solve_ivp(propagate_1d, (0, 7), [0.0,-1.0], dense_output=True, atol=1e-15, method='DOP853', max_step=0.05)
    scaled_sol = lambda t: sol.sol(t * 2 * np.pi)[0]

    assert scaled_sol(0.25) == pytest.approx(-1.0, rel=1e-4)
    assert scaled_sol(1.25) == pytest.approx(-1.0, rel=1e-4)
    
    
    
def test_eps_splines():
    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 2, 10)
    
    z = x[:, None] + y[None, :]
    
    spline2d = make_eps_splines_1d(x, y, z)
    
    assert spline2d.eps(0.5, 0.5) == pytest.approx(1.0)
    assert spline2d.depsdQ(0.5, 0.5) == pytest.approx(1.0)
    assert spline2d.depsdw(0.5, 0.5) == pytest.approx(1.0)