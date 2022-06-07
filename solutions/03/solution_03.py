# Blurring the image I_gray with two different kernels
width = 15

# Construct & apply 15x15 Gaussian kernel
gaussian_kernel = gaussian2d(7, width)
I_gauss = sp.signal.convolve2d(I_gray, gaussian_kernel, mode='same', boundary='fill')

# Construct & apply 23x23 averaging kernel
width = 23
averaging_kernel = np.ones([width, width])/(width*width)
I_ave = sp.signal.convolve2d(I_gray, averaging_kernel, mode='same', boundary='fill')

# Generate plots
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.title('Gaussian Kernel')
plt.xticks([])
plt.yticks([])
plt.imshow(I_gauss[100:228,100:228], cmap='gray')
plt.subplot(122)
plt.xticks([])
plt.yticks([])
plt.title('Averaging (Box) Kernel')
plt.imshow(I_ave[100:228,100:228], cmap='gray');