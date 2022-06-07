# Notebook 09 - Exercise 01

from scipy.spatial import distance
import numpy as np

a = np.array([1,0,0])
b = np.array([0,1,0])
c = np.array([1,1,0])
d = np.array([10,-2,1])

# Set up an m-by-n matrix, where m is the number of
# data items and n is the dimension
X = np.vstack((a,b,c,d))
#print(f'Shape of X is {X.shape}')

# D is condensed matrix
metric = ['cosine', 'euclidean']
i = 0
D = distance.pdist(X, metric[i])

# Lets convert it into square form
print(f'{metric[i]} distance:')
print(distance.squareform(D))