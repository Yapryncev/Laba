from PIL import Image
import numpy as np

img = Image.open('photo/left.jpg')

width, height = img.size

#from_points = [(0, 0), (width-1, 0), (width-1, height-1), (0, height-1)]
#new_points = [(width-1, 0), (0, 0), (0, height-1), (width-1, height-1)]

m = -0.5
xshift = abs(m)*width
new_width = width + int(round(xshift))


fin = img.transform((img.size), Image.PERSPECTIVE,(1, 200, 1, 250))
coeffs = find_coeffs(new_points, from_points)

#fin = img.transform((width,height), Image.PERSPECTIVE, new_points, Image.BICUBIC)

fin.show()
img.show()