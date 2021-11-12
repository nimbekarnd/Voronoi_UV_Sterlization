import math
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict



def find_point(width, height, n, m):
    np.random.seed(1234)
    c_x = np.random.rand(m) * width // 2
    c_y = np.random.rand(m) * height // 2

    target = []
    x_ = []
    y_ = []
    x__ = []
    y__ = []
    if n == 1:
        s_x = 0
        s_y = 0
        g_x = width //2
        g_y = height//2
        for y in range(s_y, g_y):
            y_.append(y)
        for x in range(s_x, g_x):
            x_.append(x)
        for y in range(s_y, g_y):
            for x in range(s_x, g_x):
                target.append((x,y))
        x__.append(list(c_x))
        y__.append(list(c_y))
        print(x__, y__)

    elif n == 4:
        s_x = width //2
        s_y = 0
        g_x = width
        g_y = height//2
        for y in range(s_y, g_y):
            y_.append(y)
        for x in range(s_x, g_x):
            x_.append(x)
        for y in range(s_y, g_y):
            for x in range(s_x, g_x):
                target.append((x, y))
        x__.append(list(c_x))
        for i in range(len(x__[0])):
            x__[0][i] = x__[0][i] + (width//2)
        y__.append(list(c_y))
        print(x__, y__)
    elif n == 3:
        s_x = width // 2
        s_y = height//2
        g_x = width
        g_y = height
        for y in range(s_y, g_y):
            y_.append(y)
        for x in range(s_x, g_x):
            x_.append(x)
        for y in range(s_y, g_y):
            for x in range(s_x, g_x):
                target.append((x, y))
        x__.append(list(c_x))
        for i in range(len(x__[0])):
            x__[0][i] = x__[0][i] + (width//2)
        y__.append(list(c_y))
        for j in range(len(y__[0])):
            y__[0][j] = y__[0][j] + (height//2)

    elif n == 2:
        s_x = 0
        s_y = height // 2
        g_x = width // 2
        g_y = height
        for y in range(s_y, g_y):
            y_.append(y)
        for x in range(s_x, g_x):
            x_.append(x)
        for y in range(s_y, g_y):
            for x in range(s_x, g_x):
                target.append((x, y))
        x__.append(list(c_x))
        y__.append(list(c_y))
        for j in range(len(y__[0])):
            y__[0][j] = y__[0][j] + (height//2)

    return s_x, s_y, g_x, g_y, x__[0], y__[0], target


def generate_voronoi_diagram(width, height, n, m):
    arr = np.zeros((width, height, 3), dtype=int)
    #print(arr.shape)
    s_x, s_y, g_x, g_y, c_x, c_y, target = find_point(width, height, n, m)
    imgx, imgy = g_x, g_y
    num_cells=len(c_x)

    nx = c_x
    ny = c_y

    randcolors = np.random.randint(0, 255, size=(num_cells, 3))
    cell_list = []

    for y in range(s_y, imgy):
        for x in range(s_x, imgx):
            cell_list.append((y, x))
            dmin = math.hypot(imgx-1, imgy-1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i]-x, ny[i]-y)
                if d < dmin:
                    dmin = d
                    j = i
            arr[x, y, :] = randcolors[j]
    #plt.imshow(arr.transpose(1, 0, 2))
    plt.imshow(arr)
    plt.scatter(c_y, c_x, c='w', edgecolors='k')
    plt.show()
    return arr, target


def processing_voronoi(width, height, room, regions):
    arr, target = generate_voronoi_diagram(width, height, room, regions)

    find_val = []


    for elem in arr:
        for i in range(arr.shape[1]):
            a = list(elem[i])
            if a not in find_val:
                find_val.append(a)
    #print(find_val)
    elem = find_val.index([0,0,0])
    find_val.pop(elem)
    #print(elem)

    #print(find_val)

    final = defaultdict(list)
    for k in range(len(find_val)):
        a, b = np.where(np.all(arr == find_val[k], axis=-1))
        a = list(a)
        b = list(b)
        for m in range(len(a)):
            final[k].append((a[m], b[m]))

    #print('final:', final.get(1))
    return final
#
# if __name__ == "__main__":
#     w = int(input())
#     h = int(input())
#     room = int(input())
#     regions = int(input())
#     processing_voronoi(w, h, room, regions)