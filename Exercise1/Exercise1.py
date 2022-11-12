import cv2
import numpy as np
bit_number=8  #Bit number or layer number ,,starting from one

binary_repr_v = np.vectorize(np.binary_repr)
img=cv2.imread('E:\\python\\7.numpy\\opencv\\a.jpg',0)
binaryImg=binary_repr_v(img, width=8)
shape=np.shape(img)

new_arr = []

for element in binaryImg:
    binary_number=''
    for number in  element:
       binary_number=number[8-bit_number]
       for i in range(bit_number-1):
            binary_number+='0'
       new_arr.append(int(binary_number,2))
  
a=np.reshape(new_arr,shape)
newImg=np.array(a, dtype=np.uint8)

cv2.imshow('image-1',newImg)
cv2.waitKey(0)
