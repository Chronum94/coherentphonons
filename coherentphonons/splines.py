from scipy.interpolate import RectBivariateSpline
from dataclasses import dataclass
from typing import Callable

@dataclass
class PotentialFunctions:
    e: Callable
    f: Callable
    k: Callable
    
@dataclass
class EpsilonFunctions:
    eps: Callable
    depsdQ: Callable
    depsdw: Callable


def make_pes_splines_1d(displacements, energies, spline_degree=5):
    """_summary_

    Parameters
    ----------
    energies : Iterable[float]
        Energies in eV
    displacements : Iterable[float]
        Displacements in Angstrom
    spline_degree : int, optional
        Degree of interpolation spline, by default 5

    Returns
    -------
    Tuple of splines
        A tuple containing splines of (energy, gradient of energy, curvature of energy)
    """
    s = UnivariateSpline(displacements, energies, k=spline_degree, s=0.0)
    sn = UnivariateSpline(displacements, -energies, k=spline_degree, s=0.0)
    return PotentialFunctions(s, sn.derivative(1), s.derivative(2))

def make_eps_splines_1d(displacements, energies, epsilon, spline_degree=5):
    """
    """
    sr = RectBivariateSpline(displacements, energies, epsilon.real, kx=spline_degree, ky=spline_degree, s=0.0)
    si = RectBivariateSpline(displacements, energies, epsilon.imag, kx=spline_degree, ky=spline_degree, s=0.0)
    
    dsrdq = sr.partial_derivative(1, 0)
    dsidq = si.partial_derivative(1, 0)
    
    dsrdw = sr.partial_derivative(0, 1)
    dsidw = si.partial_derivative(0, 1)
    
    eps = lambda x, w: sr(x, w) + 1.0j * si(x, w)
    depsdQ = lambda x, w: dsrdq(x, w) + 1.0j * dsidq(x, w)
    depsdw = lambda x, w: dsrdw(x, w) + 1.0j * dsrdw(x, w)

    return EpsilonFunctions(eps, depsdQ, depsdw)
