# Notebook 09 - Solution 03

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
i = 1
D = distance.squareform(distance.pdist(X, metric[i]))
print('Distance:\n', D)

# Lets convert it into square form
sigma = 0.0001
scaling = 2 * (sigma ** 2)

print(f'{metric[i]} similarity:')
np.set_printoptions(formatter={'float': lambda x: "{0:0.1e}".format(x)})
S = np.exp(-D**2 / (scaling))
print('Similarity:\n', S)
np.set_printoptions() # To not mess with other printing