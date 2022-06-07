# Notebook 09 - kdtree.py

import numpy as np
from scipy.spatial import KDTree

rng = np.random.RandomState(0)
X = rng.random_sample((10, 3))
print(X)
T = KDTree(X, leafsize=3)
distance, index = T.query(X[0,:]) # Try to perturb the query vector +[0.01,0.01,0]
print(f'distance={distance}, data={X[index,:]}')