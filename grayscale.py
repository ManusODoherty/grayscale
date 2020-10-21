"""
program: grayscale.py
Manus O'Doherty 10/13/2020

takes and image and converts it to grayscale.
"""

from images import Image

def main():
	filename = input("Please enter name of image file. Must be a GIF file >> ")
	image = Image(filename)
	print("Close the image window to continue.")
	# draw the original file
	image.draw()
	#indicate that the next phase is happening
	print("Processing image...")
	#send the original file date into the blackAndWhite function
	grayscale(image)
	print("Close the new image window to quit.")
	# draws the black and white version of the image
	image.draw()

def grayscale(image):
	"""converts the argument image to pure black and white based on the original pixel color."""
	
	# for loops to handle the row-major traversal of the pixels
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(r, g, b) = image.getPixel(x, y)
			r = int(r * 0.299)
			g = int(g * 0.587)
			b = int(b * 0.114)
			lum = r + g + b
			image.setPixel(x, y, (lum, lum, lum))

main()