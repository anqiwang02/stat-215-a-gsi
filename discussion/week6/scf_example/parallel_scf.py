from joblib import Parallel, delayed
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# define a function which takes a good amount of time to compute
def linreg_mse(p):
    mses = []
    for i in range(1000):
        X = np.random.normal(size=(int(1e4), p))
        y = np.random.normal(size=int(1e4))
        model = LinearRegression()
        model.fit(X, y)
        mses.append(model.score(X, y))
    return np.mean(mses)
# say we want to get the result for a bunch of values of p

# how we would do it non-parallel, as a list or generator:
# results = [linreg_mse(p) for p in range(10, 20)]
# results = (linreg_mse(p) for p in range(10, 20))

# we can do it in parallel using Parallel() and delayed() from joblib
results = Parallel(n_jobs=4)(delayed(linreg_mse)(p) for p in range(10, 20))
# note: it won't work if you leave out the delayed()!
# note: n_jobs can be set to -1 to use all available cores on the machine
#       be careful with doing this on your own laptop! but it's good for SCF.

# results is now a generator. lists are easier to work with.
results = list(results)

# let's not forget to save results! Here are a couple ways:

# print for posterity - this will show up in the job's output and can be useful for debugging
print(results)

# use numpy to save a text file: good for very raw outputs
np.savetxt('results.txt', results)

# use pandas to save a csv file: good for reproducibility (columns have names)
df = pd.DataFrame({'p': list(range(10,20)), 'mse': results})
df.to_csv('results.csv', index=False)
