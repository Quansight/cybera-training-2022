# Computing representation of a line from two points in homogeneous coordinates
ah = np.array([1,2,1])
bh = np.array([4,3,1])

l = np.cross(ah, bh)
print('l = {}'.format(l))
print('Computed line passes through point a: {}'.format(math.isclose(np.dot(ah, l), 0.0)))
print('Computed line passes through point b: {}'.format(math.isclose(np.dot(bh, l), 0.0)))