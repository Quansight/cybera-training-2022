# Computing a 1D convolution from scratch
f = np.array([1,3,4,1,10,3,0,1])
h = np.array([1,0,-1])
width = 1
result = np.ones(len(f)-2*width)   # Array to store computed moving averages
for i in range(len(result)):
    centre = i + width
    result[i] = np.dot(h[::-1], f[centre-width:centre+width+1])
print(f'signal f:\t\t{f}')
print(f'kernel h:\t\t{h}')
print(f'convolution (f*h):\t{result}')