import cv2
import numpy as np
from PIL import Image



SCALE = 9    #8+1


#---------------prepare image----------------

im = Image.open("input.jpg")
img = np.array(im)
img1 = np.array(im)
img1[:,:,0] = img[:,:,2]
img1[:,:,1] = img[:,:,1]
img1[:,:,2] = img[:,:,0]
img1 = img1 /255

img1 = cv2.resize(img1, (0, 0), fx=0.5, fy=0.5)
print(img1.shape)

#-----------------------initial map image---------------

map_height = ((SCALE) * img1.shape[0]) 
map_width =  ((SCALE) * img1.shape[1]) 

map1 = np.zeros((map_height, map_width, 3))
print(map1.shape)

#----------------------create map -------------------------


for i in range(img1.shape[0]):
    for j in range( img1.shape[1]):
        for k in range(SCALE):
            for l in range( SCALE):
                map1[i*SCALE+k , j*SCALE+l , :] = img1[i , j , :]
                if(l==SCALE -1 or k == SCALE -1):
                    map1[i*SCALE+k , j*SCALE+l , :] = 0
                    if(i % 10 == 0 ):
                        map1[i*SCALE , j*SCALE+l , :] = 0
                        map1[i*SCALE , j*SCALE+l , 1] = 1
                    if( j % 10 == 0):
                        map1[i*SCALE+k , j*SCALE , :] = 0
                        map1[i*SCALE+k , j*SCALE , 1] = 1
        
     

cv2.imwrite('output.jpg',map1*255) 

cv2.imshow('norm1',map1)

cv2.waitKey()


