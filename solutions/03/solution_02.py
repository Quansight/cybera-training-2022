# Computing a 1D convolution using np.convolve
f = np.array([1, 3, 4, 1, 10, 3, 0, 1])
h = np.array([1, 0, -1])
r = np.convolve(f, h, mode='valid')
print(f'signal f:\t\t{f}')
print(f'kernel h:\t\t{h}')
print(f'convolution (f*h):\t{r}')