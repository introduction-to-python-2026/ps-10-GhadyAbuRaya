from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    from PIL import Image
import numpy as np

def load_image(path):
  
    img = Image.open(path)
  
    img_array = np.array(img)
    return img_array




def edge_detection(image):
    import numpy as np
from scipy.signal import convolve2d

def edge_detection(image):
  
    if image.ndim == 3:
        grayscale = image.mean(axis=2)
    else:
        grayscale = image

    kernelY = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])
    kernelX = np.array([[-1, -2, -1],
                         [ 0,  0,  0],
                         [ 1,  2,  1]])

   
    edgeY = convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)
    edgeX = convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)

 
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG
