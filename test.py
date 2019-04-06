from PIL import Image

import numpy as np

#b = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#a = np.reshape(b,(3,3))
#for i in a:
#    print (i)
#print (a)

img = Image.new('RGB', (1920, 1080*2))
img1 = Image.open('photo/left.jpg')
img2 = Image.open('photo/right.jpg')
img.paste(img1, (0,1070))
img.paste(img2,(0,0))


img3 = img.crop((400,0, 1600, 1080*2))

img3.show()