import matplotlib.pyplot as plt 
import numpy as np

def the_eye(order):
    points = {-0.5-0.5j, 0.5+0.5j}
    k = 0
    for i in range(order-1):
        new_center = {point * 1j for point in points}
        if i % 2 == 0:
            points.update({point + (2**k)*(-1 + 1j) for point in new_center})
            points.update({point + (2**k)*(1 - 1j) for point in new_center})
        else:
            points.update({point + (2**k)*(1 + 1j) for point in new_center})
            points.update({point + (2**k)*(-1 - 1j) for point in new_center})
            k += 1
    return points

def draw(points):
    reals = [int(z.real + 0.5) for z in points]
    imags = [int(z.imag + 0.5) for z in points]

    minX = min(reals)
    minY = min(imags)

    dimension = len(set(reals))
    data = np.zeros((dimension, dimension))

    # Set elements to 1 at the indices corresponding to the complex numbers
    for real, imag in zip(reals, imags):
        data[real-minX][imag-minY] = 1

    plt.imshow(data, cmap='binary', interpolation='nearest')
    plt.axis('off')
    plt.savefig(r'C:\Users\PC\Downloads\eyes\eye17', dpi=4000)
    plt.show()

def main():
    points = the_eye(17)
    draw(points)

main()
