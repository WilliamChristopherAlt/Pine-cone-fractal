import matplotlib.pyplot as plt 
import numpy as np
import math

def the_eye(order):
    length = 1
    for i in range(order+1):
        length = length + 2**(math.floor((i+1)/2))
    points = np.zeros((length, length), dtype=bool)

    center = int(length/2)
    points[center, center] = points[center-1, center-1] = True

    nudge = 1
    for i in range(order):
        rotated = np.rot90(points)
        if i % 2 == 0:
            points = points | np.roll(rotated, (-nudge, nudge), axis=(0, 1)) | np.roll(rotated, (nudge, -nudge), axis=(0, 1))
        else:
            points = points | np.roll(rotated, (nudge, nudge), axis=(0, 1)) | np.roll(rotated, (-nudge, -nudge), axis=(0, 1))
            nudge *= 2
    return points

def draw(points):
    plt.imshow(points, cmap='binary', interpolation='nearest')
    plt.axis('off')
    # plt.savefig(r'C:\Users\PC\Downloads\eye20', dpi=2000)
    plt.show()

def main():
    points = the_eye(15)
    draw(points)

main()
