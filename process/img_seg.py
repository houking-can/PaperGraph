
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import time

def segmentation(image):

    return None


def decode_segmap(image, nc=21):
    label_colors = np.array(
        [
            (0, 0, 0),  # 0=background
            # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
            (128, 0, 0),
            (0, 128, 0),
            (128, 128, 0),
            (0, 0, 128),
            (128, 0, 128),
            # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
            (0, 128, 128),
            (128, 128, 128),
            (64, 0, 0),
            (192, 0, 0),
            (64, 128, 0),
            # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
            (192, 128, 0),
            (64, 0, 128),
            (192, 0, 128),
            (64, 128, 128),
            (192, 128, 128),
            # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
            (0, 64, 0),
            (128, 64, 0),
            (0, 192, 0),
            (128, 192, 0),
            (0, 64, 128),
        ]
    )

    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)

    for i in range(0, nc):
        idx = image == i
        r[idx] = label_colors[i, 0]
        g[idx] = label_colors[i, 1]
        b[idx] = label_colors[i, 2]

    rgb = np.stack([r, g, b], axis=2)
    rgb = Image.fromarray(rgb)

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    path = "./media/processed_images/" + now + r".jpg"
    path = os.path.abspath(path)
    rgb.save(path)

    path = "\\" + os.path.relpath(path)
    return path.replace("\\", "/")


def main():
    pass


if __name__ == "__main__":
    main()
