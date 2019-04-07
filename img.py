import numpy as np
import cv2
from PIL import Image
import matplotlib as plt
test = 'photo\left.jpg'
img = Image.open(test)


#width, height = img.size #Get dimensions
#left = width/2
#top = 3*height/2
#right = width/2
#bottom = 3*height/3
#cropped_example = img.crop((left, top, right, bottom))

#cropped_example.show()

def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype = numpy.float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)


rows, cols, ch = img.shape[0], img.shape[1], img.shape[2]

#pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
#pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

#M = cv2.getPerspectiveTransform(pts1,pts2)

#dst = cv2.warpPerspective(img,M,(300,300))

#plt.subplot(121),plt.imshow(img),plt.title('Input')
#plt.subplot(122),plt.imshow(dst),plt.title('Output')
#plt.show()

#coeffs = find_coeffs(
#        [(0, 0), (256, 0), (256, 256), (0, 256)],
#        [(0, 0), (256, 0), (new_width, height), (xshift, height)])
#
#img.transform((width, height), Image.PERSPECTIVE, coeffs, Image.BICUBIC).save(sys.argv[3])

#find_coeffs(74.99999999, 74.99999)

def transform(startpoints, endpoints, im):
    width, height = im.size
    coeffs = find_coeffs(endpoints, startpoints)

    im = im.transform((width,height), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    return im

