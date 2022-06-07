# Notebook 7 - Exercise 2

level = 0
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)
plt.figure(figsize=(10,5))
plt.suptitle('Level = {}'.format(level))
plt.subplot(121)
plt.title('Image')
plt.xticks([])
plt.yticks([])
plt.imshow(gray, cmap='gray')
plt.subplot(122)
plt.title('Harris corner response')
plt.imshow(dst, cmap='gray')
plt.xticks([])
plt.yticks([])