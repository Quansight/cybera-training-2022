# Determining extrinsic & intrinsic parameters of camera from a projection matrix.

# Extract the leading 3x3 block of P as M
M = P[:3,:3]
print('M:\n {}'.format(M))

# Compute the RQ decomposition from M with scipy.linalg.rq
K, R = linalg.rq(M)
print('K:\n {}'.format(K))
print('R:\n {}'.format(R))

# Lets ensure that the diagonal entries of $\mathtt{K}$ are positive.

sgn = np.sign(np.diag(K))
K_new = np.dot(K, np.diag(sgn))
R_new = np.dot(np.diag(sgn), R)
print('K_new:\n {}'.format(K_new))
print('R_new:\n {}'.format(R_new))

# *Aside*
#
# The above is valid we are simply replacing $\mathtt{K} \mathtt{R}$ with $\mathtt{K} \mathbf{I} \mathtt{R}$.  See below.

print(np.dot(np.diag(sgn), np.diag(sgn)))

# Let's find camera center (the easy way)

C = - np.dot(np.linalg.inv(M), P[:,3])

print('C:\n {}'.format(C))

# Now the hard way.  Recall that camera center is the right null-space of $\mathtt{P}$

C = linalg.null_space(P)
C = C[:3] / C[3,0]
print('C:\n {}'.format(C.flatten()))

# Another way: use the SVD.  Keeps you fighting fit.

U, s, Vh = np.linalg.svd(P)

#print('U:\n {}'.format(U))
#print('s:\n {}'.format(s))
#print('Vh:\n {}'.format(Vh))

C = Vh[3,:] # Last column of V
C = C[:3] / C[3]
print('C:\n {}'.format(C.flatten()))