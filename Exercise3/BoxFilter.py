import cv2
import numpy as np
def boxFillter(img):
    

    shape=np.shape(img)
    box_fillter=np.array([[1,1,1,1,1],
                      [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1]
                     ])

    shape_boxFillter=box_fillter.shape
    index_middle=shape_boxFillter[0]//2

    row,col=img.shape
    newIMG=[]
    for i in range(row):
        for j in  range(col):
            x1=0
            x2=0
            y1=0
            y2=0
            if (shape_boxFillter[0]-index_middle)<=i:
                x1=i-(shape_boxFillter[0]-index_middle)
            else:
                x1=0
        
            if (shape_boxFillter[0]-index_middle)<=row-i:
                x2=i+(shape_boxFillter[0]-index_middle)
            else:
                x2=row


            if (shape_boxFillter[0]-index_middle)<=j:
                y1=j-(shape_boxFillter[0]-index_middle)
            else:
                y1=0
        
            if (shape_boxFillter[0]-index_middle)<=col-j:
                y2=j+(shape_boxFillter[0]-index_middle)
            else:
                y2=col
        
            matrix=np.array(img[x1:x2-1,y1:y2-1])
            a=(matrix.sum())
            b=box_fillter.sum()
            c=a//b
            newIMG.append(c) 

    a=np.reshape(newIMG,shape)
    newImg=np.array(a, dtype=np.uint8)
    return newImg
    # cv2.imshow('image-1',newImg)
    # cv2.waitKey(0)
