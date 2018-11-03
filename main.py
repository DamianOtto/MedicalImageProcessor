import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aaa.jpeg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
int_array, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(thresh1, contours,-1,(0,255,0), 3)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

plt.imshow(thresh1)

#for i in range(6):
 #   plt.subplot(2,3,i+1),\
  #  plt.imshow(images[i])
   # plt.title(titles[i])
    #plt.xticks([]),plt.yticks([])

plt.show()

