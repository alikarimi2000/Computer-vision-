
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageChops
import BoxFilter
img0 = cv2.imread('E:\\python\\7.numpy\\opencv\\a.jpg',0)


img = cv2.GaussianBlur(img0,(3,3),0)


laplacian = cv2.Laplacian(img,cv2.CV_64F)

sumImgAndLap=np.add(img,laplacian)

sobelx64f = cv2.Sobel(img0,cv2.CV_64F,0,1,ksize=3)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f )



dst=BoxFilter.boxFillter(img)

f=dst*laplacian
# f=np.uint8(abs_sobel64f )
f=f+abs(f.min())
f=(f/ f.max())*255
f=np.uint8(abs_sobel64f )
g=np.add(img,f)


gamma_two_point_two = np.array(255*(g/255)**.8,dtype='uint8')


plt.subplot(2,4,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3),plt.imshow(sumImgAndLap,cmap = 'gray')
plt.title('Laplacian image+normal image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('sobelx'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,5),plt.imshow(dst,cmap = 'gray')
plt.title('BoxFilter'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6),plt.imshow(f,cmap = 'gray')
plt.title('f'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7),plt.imshow(g,cmap = 'gray')
plt.title('g'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8),plt.imshow(gamma_two_point_two,cmap = 'gray')
plt.title('h'), plt.xticks([]), plt.yticks([])

plt.show()
