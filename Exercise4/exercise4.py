import numpy as np
from scipy import misc
from scipy import fftpack
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw,ImageOps,ImageFilter
from pylab import figure, title, imshow, hist, grid,show

im=Image.open("E:\\openCv\\Computer-vision-\\Exercise4\\4.jpg").convert('L') 
img=np.array(im)
h,w = img.shape

kernel=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])


sz = (img.shape[0] - kernel.shape[0], img.shape[1] - kernel.shape[1])  # total 

kernel = np.pad(kernel, (((sz[0]+1)//2, sz[0]//2), ((sz[1]+1)//2, sz[1]//2)), 
'constant')
print(kernel)
kernel = fftpack.ifftshift(kernel)
print(kernel)
filtered = np.real(fftpack.ifft2(fftpack.fft2(img) * 
fftpack.fft2(kernel)))+np.imag(fftpack.ifft2(fftpack.fft2(img) * 
fftpack.fft2(kernel)))
filtered=np.maximum(0,np.minimum(filtered,255))
im2=Image.open("E:\\openCv\\Computer-vision-\\Exercise4\\4.jpg").convert('L') 

u=im2.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 
scale=1, offset=0))

fig2=figure()

ax1 = fig2.add_subplot(221)  
ax2 = fig2.add_subplot(222)
ax3 = fig2.add_subplot(223)

ax1.title.set_text('Original Image')
ax2.title.set_text('After convolving in freq domain')
ax3.title.set_text('imagefilter conv')
ax1.imshow(img,cmap='gray')
ax2.imshow(filtered,cmap='gray')
ax3.imshow(np.array(u),cmap='gray')

show()