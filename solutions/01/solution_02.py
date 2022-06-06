# Computing point of intersection of two lines using homogeneous coordinates
ah = np.array([3,-1,7])
bh = np.array([3,-1,-3])

p = np.cross(ah, bh)
print('p = {}'.format(p))
print('Homogenous component of p: w = {}'.format(p[2]))
print('Computed line passes through point a: {}'.format(math.isclose(np.dot(ah, p), 0.0)))
print('Computed line passes through point b: {}'.format(math.isclose(np.dot(bh, p), 0.0)))
