# loading an image from the previously constructed list of filepaths images.
img = cv.imread(images[0]) # Extract the first image as img
print(img.shape)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Convert to a gray scale image
print(img.shape, gray.shape)
plt.imshow(gray, cmap='gray'); # Visualize gray