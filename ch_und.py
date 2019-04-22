import numpy as np
import cv2
import sys
from pathlib import Path
from PIL import Image
import ch_und

class Fishimage:
#DIM=(1920, 1080)
#K=np.array([[942.1405901425625, 0.0, 972.6199914509249], [0.0, 942.4205473015921, 523.6775993168499], [0.0, 0.0, 1.0]]) # оригинал
#D=np.array([[-0.029226448287922854], [0.15203494417092783], [-0.526623632539975], [0.6165219736008233]]) # оригинал

# balance от 0 до 1

   def __init__ (self, res_img1, res_img, imgN, imgV):
      self.res_img = res_img
      self.res_img1 = res_img1
      self.imgN = imgN
      self.imgV = imgV

   def understortN(self, balance = 0, dim2 = None, dim3 = None):
      K = np.array( [[900.1405901425625, 0.0, 1000.6199914509249], [0.0, 850.4205473015921, 723.6775993168499], [1.0, 0.0, 0.0]])
      D = np.array([[0.126448287922854], [0.38203494417092783], [-1.026623632539975], [0.6165219736008233]])
      #K = np.array([[942.1405901425625, 0.0, 972.6199914509249], [0.0, 942.4205473015921, 523.6775993168499], [0.0, 0.0, 1.0]])  # оригинал
      #D = np.array([[-0.029226448287922854], [0.15203494417092783], [-0.526623632539975], [0.6165219736008233]]) # оригинал
      DIM = (1920, 1080)
      img = cv2.imread('img\img1.jpg')
      dim1 = img.shape[:2][::-1]  # dim1 is the dimension of input image to un-distort
      # assert dim1[0]/dim1[1] == DIM[0]/DIM[1], #"Image to undistort needs to have same aspect ratio as the ones used in calibration"
      if not dim2:
         dim2 = dim1
      if not dim3:
         dim3 = dim1
      scaled_K = K * dim1[0] / DIM[0]  # The values of K is to scale with image dimension.
      scaled_K[2][2] = 1.0  # Except that K[2][2] is always 1.0
      # This is how scaled_K, dim2 and balance are used to determine the final K used to un-distort image. OpenCV document failed to make this clear!
      new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(scaled_K, D, dim1, np.eye(3), balance=balance)
      map1, map2 = cv2.fisheye.initUndistortRectifyMap(scaled_K, D, np.eye(3), new_K, dim3, cv2.CV_16SC2)
      self.res_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
      #cv2.imshow("undistorted", self.res_img)
      #cv2.imwrite('C:\prog\photo\imgWWW.jpg' ,self.res_img)

      cv2.waitKey(0)
      cv2.destroyAllWindows()
      #return res_img


   def understortV(self, balance = 0, dim2=None, dim3=None):
      K = np.array([[852.1405901425625, 0.0, 970.6199914509249], [0.0, 942.4205473015921, 603.6775993168499], [0.0, 0.0, 1.0]])  # оригинал
      D=np.array([[0.129226448287922854], [0.15203494417092783], [-0.426623632539975], [0.6165219736008233]])
      #K = np.array([[942.1405901425625, 0.0, 972.6199914509249], [0.0, 942.4205473015921, 523.6775993168499],[0.0, 0.0, 1.0]])  # оригинал
      #D=np.array([[-0.029226448287922854], [0.15203494417092783], [-0.526623632539975], [0.6165219736008233]]) # оригинал
      #K = np.array([[942.1405901425625, 0.0, 972.6199914509249], [0.0, 942.4205473015921, 503.6775993168499], [0.0, 0.0, 1.0]])
      #D = np.array([[-0.029226448287922854], [0.25203494417092783], [-0.526623632539975], [0.4165219736008233]])
      DIM = (1920, 1080)
      img1 = cv2.imread('img\img2.jpg')
      dim1 = img1.shape[:2][::-1]  # dim1 is the dimension of input image to un-distort
      # assert dim1[0]/dim1[1] == DIM[0]/DIM[1], #"Image to undistort needs to have same aspect ratio as the ones used in calibration"
      if not dim2:
         dim2 = dim1
      if not dim3:
         dim3 = dim1
      scaled_K = K * dim1[0] / DIM[0]  # The values of K is to scale with image dimension.
      scaled_K[2][2] = 1.0  # Except that K[2][2] is always 1.0
      # This is how scaled_K, dim2 and balance are used to determine the final K used to un-distort image. OpenCV document failed to make this clear!
      new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(scaled_K, D, dim1, np.eye(3), balance=balance)
      map1, map2 = cv2.fisheye.initUndistortRectifyMap(scaled_K, D, np.eye(3), new_K, dim3, cv2.CV_16SC2)
      self.res_img1 = cv2.remap(img1, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
      #cv2.imshow("undistorted", self.res_img1)
      #    cv2.imwrite('C:\opencv\prog\photos\img4.jpg' ,res_img1)

      cv2.waitKey(0)
      cv2.destroyAllWindows()
#      return res_img1

   def warpN(self):
      rect = np.zeros((4, 2), dtype="float32")
      #rect = np.array(([520, 78], [1720, 48], [1629, 1042], [685, 1010]), dtype="float32")
      rect = np.array(([604, 433], [1720, 48], [1629, 1042], [685, 1010]), dtype="float32") #var1
      #dst = np.array(([610, 35], [1732, 48], [1669, 1042], [675, 1010]), dtype="float32") #var2
      dst = np.array(([590, 260], [1860, 0], [2050, 1042], [520, 1010]), dtype="float32")  # var3
      #dst = np.array(([520, 78], [1720, 48], [1629, 1042], [685, 1010]), dtype="float32")
      #dst = np.array(([507, 56], [1732, 48], [1629, 1042], [600, 1010]), dtype="float32") #var1
      #dst = np.array(([560, 86], [1750, 48], [1645, 1042], [678, 1010]), dtype="float32")
      M = cv2.getPerspectiveTransform(rect, dst)
      self.imgN = cv2.warpPerspective(self.res_img, M, (1920, 1080))

      #pect = np.zeros((4, 2), dtype="float32")
      #pect = np.array(([520, 78], [1720, 344], [1629, 1042], [685, 1010]), dtype="float32")
      #pst = np.array(([610, 55], [1700, 344], [1669, 1042], [675, 1010]), dtype="float32")
      # dst = np.array(([507, 56], [1732, 48], [1629, 1042], [600, 1010]), dtype="float32") #var1
      # dst = np.array(([560, 86], [1750, 48], [1645, 1042], [678, 1010]), dtype="float32")
      #N = cv2.getPerspectiveTransform(pect, pst)
      #self.imgN = cv2.warpPerspective(self.res_img, N, (1920, 1080))

      #cv2.imshow("Original", image)
      #cv2.imshow("Warped", warped)
      #cv2.imwrite('C:\opencv\prog\photos\imgWW.jpg', self.res_img)

      cv2.waitKey(1)

   def warpV(self):
      rect = np.zeros((4, 2), dtype="float32")

      rect = np.array(([569, 60], [1615, 71], [1590, 824], [661, 999]), dtype="float32")
      dst = np.array(([619, 50], [1735, 71], [1770, 823], [661, 1055]), dtype="float32")
      #dst = np.array(([569, 60], [1708, 25], [1635, 1001], [661, 999]), dtype="float32") #fin
      #dst = np.array(([569, 60], [1708, 25], [1621, 1001], [661, 999]), dtype="float32") var 2
      #dst = np.array(([569, 60], [1708, 25], [1621, 1001], [611, 999]), dtype="float32") #var1
      #dst = np.array(([569, 40], [1562, 25 - 20], [1708, 1001 - 20], [589, 913]), dtype="float32")
      M = cv2.getPerspectiveTransform(rect, dst)
      self.imgV = cv2.warpPerspective(self.res_img1, M, (1920, 1080))

      cv2.destroyAllWindows()

      #cv2.imshow("Original", image)
      #cv2.imshow("Warped", self.imgV)
#      cv2.imwrite('C:\opencv\prog\photos\imgV.jpg', warped)
      #cv2.waitKey(0)

   def stitch(self):
      img_new = Image.new('RGB', (1920, 1080 * 2))
      self.imgV[..., [0, 2]] = self.imgV[..., [2, 0]]
      self.imgN[..., [0, 2]] = self.imgN[..., [2, 0]]
      img1 = Image.fromarray(self.imgN)
      img2 = Image.fromarray(self.imgV)

      img_new.paste(img2, (0, 0))
      img_new.paste(img1, (0, 900))

      area = ( 600, 5, 1890, 1980 )
      cropped_img = img_new.crop(area)
      cropped_img.save('img\Res.jpg')
      #img_new.show('C:\prog\photo\img_new.jpg')
      #img_new.save('C:\prog\photo\img_new.jpg')


if __name__ == '__main__':
   #for p in sys.argv[1:]:
   FH = Fishimage(None, None, None, None)
   FH.understortV()
   FH.understortN()
   FH.warpV()
   FH.warpN()
   FH.stitch()

