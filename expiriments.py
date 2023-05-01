import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgPath = "./static/images/d.png"

maxVal = 0

#remove ` (backtick not apostrophe) from before the .
#scale = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{{C}}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
scale = " .-':_,^=;+!rc*z?sLTv)J7(|FiCfI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%@"
output = ""

img = cv.imread(imgPath)
#img = cv.imread('./Duck.png')
height, width, depth = img.shape
scale_factor = 15

img = cv.resize(img, (int(width/scale_factor), int(height/scale_factor)), interpolation = cv.INTER_AREA)
width = int(width/scale_factor)
height = int(height/scale_factor)
#cv.imshow('image',img)

contrast = 1
brightness = 25

img = cv.addWeighted( img, contrast, img, 0, brightness)

sharpen_filter=np.array([[-1,-1,-1],
                [-1,9,-1],
                [-1,-1,-1]])
# applying kernels to the input image to get the sharpened image
img=cv.filter2D(img,-1,sharpen_filter)

"""alpha = 1.3
beta = .5
img = alpha*img + beta"""

#cv.imshow('image',img)

#cv.waitKey(0)




for i in range(height):
    for j in range(width):
        greyVal = int(img[i,j][0]) + int(img[i,j][1]) + int(img[i,j][2]) /3
        if greyVal > maxVal:
            maxVal = greyVal
        #img[i,j] = greyVal
        output += scale[int(float(greyVal)/600 * len(scale))]
    output += "\n"
print(maxVal)

#cv.imshow('image',img)

#cv.waitKey(0)

text_file = open("/Output.txt", "w")

text_file.write(output)

text_file.close()