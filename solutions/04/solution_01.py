I = cv.imread('data/apple.jpg')
I = cv.cvtColor(I, cv.COLOR_BGR2RGB)

print('Shape of I = {}'.format(I.shape))
I[:,:,0] = cv.GaussianBlur(I[:,:,0], (5,5), 2, 2)
I[:,:,1] = cv.GaussianBlur(I[:,:,1], (5,5), 2, 2)
I[:,:,2] = cv.GaussianBlur(I[:,:,2], (5,5), 2, 2)

I2 = I[::2,::2,:]
print('Shape of I2 = {}'.format(I2.shape))

plt.imshow(I2)