import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from image_utils import load_image, edge_detection

from skimage.filters import median
from skimage.morphology import disk

def main():
    img = load_image("your_image.jpg").astype(np.float32)

    gray = img.mean(axis=2)

    clean_gray = median(gray, footprint=disk(3))

    edgeMAG = edge_detection(clean_gray)

    thresh = np.percentile(edgeMAG, 90)
    edge_binary = (edgeMAG >= thresh).astype(np.uint8) * 255

    plt.figure()
    plt.hist(edgeMAG.ravel(), bins=256)
    plt.show()

    plt.figure()
    plt.imshow(edge_binary, cmap="gray")
    plt.axis("off")
    plt.show()

    Image.fromarray(edge_binary).save("my_edges.png")

if __name__ == "__main__":
    main()

