import numpy as np
import cython
from numba import jit
import time

# let's experiment with how to write faster code in python
# our test function is simply an addition of two numpy matrices

# the slow functions add the two matrices using a double
# for-loop.

# the fast functions just use numpy's built-in matrix addition.

# for slow and fast functions, we try also making versions
# which are compiled with cython and numba. this is done using
# the @cython and @jit "decorators", which are placed immediately
# above the functions.

def slow(a, b):
    c = np.zeros_like(a)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i, j] = a[i, j] + b[i, j]
    return c

@cython.compile
def slow_cython(a, b):
    c = np.zeros_like(a)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i, j] = a[i, j] + b[i, j]
    return c

@jit
def slow_numba(a, b):
    c = np.zeros_like(a)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i, j] = a[i, j] + b[i, j]
    return c

# now let's write functions taking advantage of the fact
# that a and b are numpy matrices

def fast(a, b):
    return a + b

# we should not expect any speedup from cython
# as it only works with base python objects,
# but we will be passing in numpy arrays.
@cython.compile
def fast_cython(a, b):
    return a + b

# we shouldn't expect much improvement from numba
# as the function is incredibly simple
@jit
def fast_numba(a, b):
    return a + b

a = np.random.rand(2000, 2000)
b = np.random.rand(2000, 2000)

# run cython and numpy functions once so they compile
# before we measure their runtime
slow_cython(a, b)
slow_numba(a, b)
fast_cython(a, b)
fast_numba(a, b)

start = time.time()
slow(a, b)
print("slow:", time.time() - start)

start = time.time()
slow_cython(a, b)
print("slow_cython:", time.time() - start)

start = time.time()
for i in range(100):
    slow_numba(a, b)
print("slow_numba:", (time.time() - start)/100)

start = time.time()
for i in range(100):
    fast(a, b)
print("fast:", (time.time() - start)/100)

start = time.time()
for i in range(100):
    fast_cython(a, b)
print("fast_cython:", (time.time() - start)/100)

start = time.time()
for i in range(100):
    fast_numba(a, b)
print("fast_numba:", (time.time() - start)/100)
