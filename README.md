# Coherent Phonons

This is a minimal package for the simulation of coherent phonons. A barebones example goes like so:

```python
import coherentphonons as p
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.1, 0.1, 7)
e = 50 * x ** 2# + 2 * x ** 3
a = p.make_splines_1d(x, e)

propagator = p.make_propagator_1d(a, 10.0, 2)
sol = p.solve(propagator, (0, 30), [0.01, 0.0])

tfine = np.linspace(0, 30, 1000)
plt.plot(tfine, sol.sol(tfine)[0])
plt.show()
```

TODO:

- [ ] Document units.
- [ ] Support multidimensional potential energy functions/propagators.

This is effectively research code and I add features/change API specifications quite often and aggressively. Use with care, reviews appreciated.
