# creates a list of strings of filepaths to image files
import glob
images = sorted(glob.glob('data/left??.jpg'))
print(images)