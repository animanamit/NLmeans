import numpy as np
from skimage.io import imread, imsave

from os.path import normpath as fn # Fixes window/linux path conventions
import warnings
warnings.filterwarnings('ignore')

def clip(im):
    return np.maximum(0.,np.minimum(1.,im))

no_noise = np.float32(imread(fn('lenaTest1.jpg')))/255.

noise_25 = np.float32(imread(fn('Lena-noise-25.png')))/255.

# comparison = np.float32((imread(fn('prob4_1_rep.jpg'))))/255.

x = 250
y = 180
sz = 128
cropped1 = no_noise[y:y+sz,x:x+sz]
cropped2 = noise_25[y:y+sz,x:x+sz]

# cropped3 = comparison[y:y+sz,x:x+sz]

imsave(fn('nonoise_ovr.jpg'),clip(cropped1))
imsave(fn('25noise_ovr.jpg'),clip(cropped2))
# imsave(fn('noisycomp.jpg'),clip(cropped3))
