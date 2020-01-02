import numpy as np
from skimage.io import imread, imsave

def nlmeans(img,sigma, big, small):


    # make a padded image
    # reds = np.pad(img[:,:,0],10,mode="constant",constant_values=0)
    # greens = np.pad(img[:,:,1],10,mode="constant",constant_values=0)
    # blues = np.pad(img[:,:,2],10,mode="constant",constant_values=0)

    # img_ = np.zeros((h+20,w+20,3))
    # img_[:,:,0] = reds
    # img_[:,:,1] = greens
    # img_[:,:,2] = blues

    # convert to greyscale
    # img_ = np.zeros_like(img[:,:,0])
    # img_ = (img[:,:,0] + img[:,:,1] + img[:,:,2])/3

    # large window of pixels around center pixel to compare to
    # is 21 x 21
    largestride = big
    smallstride = small
    pad = largestride+smallstride

    img_ = np.pad(img, pad, mode="reflect")

    newimg = np.zeros((img.shape[0], img.shape[1]))
    h,w = img_.shape

    hh = 1.5

    for y in range(pad, h-pad):
        for x in range(pad, w-pad):

            # DO EXPERIMENTS ON 128 x 128
            #select a pixel
            current = 0

            # get large window
            startY = y-largestride
            endY = y + largestride

            startX = x-largestride
            endX = x + largestride

            Z = 0

            maxweight = 0

            # go through each pixel in neighbourhood
            for yp in range(startY, endY):
                for xp in range(startX, endX):
                    
                    window1 = img_[y-smallstride:y+smallstride, x-smallstride:x+smallstride].copy()
                    window2 = img_[yp-smallstride:yp+smallstride, xp-smallstride:xp+smallstride].copy()

                    diff = np.sum((window1-window2)**2) + 2*(sigma**2)
 
                    weight = np.exp(-diff/(hh**2))

                    if weight > maxweight:
                        maxweight = weight
                    
                    if (y == yp) and (x == xp):
                        weight = maxweight

                    Z += weight
                    current = current + weight*img_[yp,xp]

            newimg[y-pad,x-pad] = current/Z

    return newimg


####
from os.path import normpath as fn # Fixes window/linux path conventions
import warnings
warnings.filterwarnings('ignore')

def clip(im):
    return np.maximum(0.,np.minimum(1.,im))

img1 = np.float32(imread(fn('25noise_cropped.jpg')))/255.
result = nlmeans(img1,25,10,9)
imsave(fn('testingh_5.jpg'),clip(result))

# img1 = np.float32(imread(fn('25noise_cropped.jpg')))/255.

# result = nlmeans(img1,25,15,3)
# imsave(fn('denoise_25_15_3.jpg'),clip(result))

# result = nlmeans(img1,25,20,3)
# imsave(fn('denoise_25_20_3.jpg'),clip(result))

# result = nlmeans(img1,25,10,6)
# imsave(fn('denoise_25_10_6.jpg'),clip(result))

# result = nlmeans(img1,25,10,9)
# imsave(fn('denoise_25_10_9.jpg'),clip(result))

