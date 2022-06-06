# Extract the corners and the return value
retval, corners = cv.findChessboardCorners(image=gray, patternSize=(9,6))
print(corners.shape)
corners = np.squeeze(corners) # Get rid of extraneous singleton dimension
print(corners.shape)
print(corners[:5])  #Examine the first few rows of corners