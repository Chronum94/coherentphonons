from scipy.interpolate import UnivariateSpline
from dataclasses import dataclass


@dataclass
class PotentialFunctions:
    e: UnivariateSpline
    f: UnivariateSpline
    k: UnivariateSpline


def make_splines_1d(displacements, energies, spline_degree=5):
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