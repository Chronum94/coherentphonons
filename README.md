# Coherent Phonons

This is a minimal package for the simulation of coherent phonons. A barebones example goes like so:

```python
import coherentphonons as p
import coherentphonons.splines as psp
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.1, 0.1, 7)
e = 50 * x ** 2# + 2 * x ** 3
a = psp.make_pes_splines_1d(x, e)

propagator = p.make_propagator_1d(a, 10.0, 2)
sol = p.solve(propagator, (0, 30), [0.01, 0.0])

tfine = np.linspace(0, 30, 1000)
plt.plot(tfine, sol.sol(tfine)[0])
plt.show()
```

TODO:

- [ ] Document units. Maybe use pint.
- [ ] Support multidimensional potential energy functions/propagators. What is a good way to do this? I currently use radial basis functions in my personal code.
- [ ] High dimensional PES training using small neural nets.
- [ ] Ensemble excitations for Poincare surfaces of sections.
- [ ] More tests. What integration tests? How would that even happen?
- [ ] A few examples, both insulating, dispersive and insulating, and dissipative+dispersive.

This is effectively research code and I add features/change API specifications quite often and aggressively. Use with care, reviews appreciated.
