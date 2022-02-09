# Pmf Moments

This is a numpy implementation to compute the first three moments of a discrete multivariate probability mass function.
In order to obtain the moments, you just have to create a pmf object and call the methods (at the moment only the first one has been implemented):

```py
import numpy as np

prob = np.ones((2,4,6))
prob /= np.sum(prob)

obj = pmf(prob)

first_moments = obj.get_first_moment()
```

The probability given as input should be thought of as a multidimensional grid (a tensor, if you prefer).
Therefore, the number of variables is arbitrary.

Since this repo is thought to be used for a pmf representing a grid of particles of different species, in the current implementation the domains of the variables are retrieved directly from the pmf and they coincide with the index of each axis, i.e. they range from 0 to the (maximum value - 1) of each species.
Maybe one day I will generalize it to completely arbitrary domains (feel free to make a pull request if you want).
