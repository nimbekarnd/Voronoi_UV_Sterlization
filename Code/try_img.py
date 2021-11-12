import numpy as np
import cv2
from PIL import Image
import time
import areaalgo as A
# from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
# import random
import sys

area = A.Area
image = Image.open('/home/ndnupur/Desktop/voronoi/Code/images/test_fff.png')
array = np.asarray(image)
map_array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
#print(map_array.shape)

map_ = np.zeros((map_array.shape[0], map_array.shape[1]), dtype=int)
mid_point = (map_.shape[0] // 2, map_.shape[1] // 2)


def room(i):
    switch_ = {1: 'Room 1', 2: 'Room 2', 3: 'Room 3', 4: 'Room 4'}
    return switch_.get(i)


def ran_ob(curr):

    obstacle1 = []
    for i in range(2, 4):
        for j in range(0, 4):
            obstacle1.append((i, j))
    for i in obstacle1:
        if curr[0] == i[0] and curr[1] == i[1]:
            return True
        return False, obstacle1


def r_space(case):
    cent_p = {}
    reg = {}
    if case == 'Room 1':
        region = []
        for i in range(0, mid_point[0]):
            for j in range(0, mid_point[1]):
                region.append((i, j))
                cent_p[case] = ((mid_point[0] // 2), (mid_point[1] // 2))
        reg[case] = region
    elif case == 'Room 2':
        region = []
        for i in range(0, mid_point[0]):
            for j in range(mid_point[1], (map_.shape[1])):
                region.append((i, j))
                cent_p[case] = ((mid_point[0] // 2), ((mid_point[1] + map_.shape[1]) // 2))
        reg[case] = region
    elif case == 'Room 3':
        region = []
        for i in range(mid_point[0], (map_.shape[0])):
            for j in range(mid_point[1], (map_.shape[1])):
                region.append((i, j))
                cent_p[case] = (((mid_point[0] + map_.shape[0]) // 2), ((mid_point[1] + map_.shape[1]) // 2))
        reg[case] = region
    elif case == 'Room 4':
        region = []
        for i in range(mid_point[0], (map_.shape[0])):
            for j in range(0, (mid_point[1])):
                region.append((i, j))
                cent_p[case] = (((mid_point[0] + map_.shape[0]) // 2), (mid_point[1] // 2))
        reg[case] = region
    else:
        sys.exit()
    return region, cent_p, reg


def check_room(node, room):
    list = room
    for chk in list:
        if node[0] == chk[0] and node[1] == chk[1]:
            return True
        else:
            return False


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def val(node, i):
    map_new = map_
    ob, obstacle = ran_ob(node)
    node_list = []
    if i == 1:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(2))[2]
        ob_cur.extend(x[room(2)])
        y = r_space(room(3))[2]
        ob_cur.extend(y[room(3)])
        z = r_space(room(4))[2]
        ob_cur.extend(z[room(4)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 1
    elif i == 2:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(1))[2]
        ob_cur.extend(x[room(1)])
        y = r_space(room(3))[2]
        ob_cur.extend(y[room(3)])
        z = r_space(room(4))[2]
        ob_cur.extend(z[room(4)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 1
    if i == 3:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(2))[2]
        ob_cur.extend(x[room(2)])
        y = r_space(room(1))[2]
        ob_cur.extend(y[room(1)])
        z = r_space(room(4))[2]
        ob_cur.extend(z[room(4)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 1
    if i == 4:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(2))[2]
        ob_cur.extend(x[room(2)])
        y = r_space(room(3))[2]
        ob_cur.extend(y[room(3)])
        z = r_space(room(1))[2]
        ob_cur.extend(z[room(1)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 1
    # print(reg_)
    for node in check_:
        node_list.append(node)
        map_new[(node[0], node[1])] = 0
        if node[0] == c[0] and node[1] == c[1]:
            map_new[(node[0], node[1])] = 1
    final = intersection(node_list, obstacle)
    for item in final:
        map_new[(item[0], item[1])] = 1

    return map_new, node_list, c


def image_c(node, i):
    map_new = map_
    ob, obstacle = ran_ob(node)
    node_list = []
    if i == 1:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(2))[2]
        ob_cur.extend(x[room(2)])
        y = r_space(room(3))[2]
        ob_cur.extend(y[room(3)])
        z = r_space(room(4))[2]
        ob_cur.extend(z[room(4)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 0
    elif i == 2:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(1))[2]
        ob_cur.extend(x[room(1)])
        y = r_space(room(3))[2]
        ob_cur.extend(y[room(3)])
        z = r_space(room(4))[2]
        ob_cur.extend(z[room(4)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 0
    if i == 3:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(2))[2]
        ob_cur.extend(x[room(2)])
        y = r_space(room(1))[2]
        ob_cur.extend(y[room(1)])
        z = r_space(room(4))[2]
        ob_cur.extend(z[room(4)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 0
    if i == 4:
        check_, cent, reg_ = r_space(room(i))
        c = cent[room(i)]
        ob_cur = []
        x = r_space(room(2))[2]
        ob_cur.extend(x[room(2)])
        y = r_space(room(3))[2]
        ob_cur.extend(y[room(3)])
        z = r_space(room(1))[2]
        ob_cur.extend(z[room(1)])

        # print('ob_cur',ob_cur)
        for node in ob_cur:
            map_new[(node[0], node[1])] = 0
    # print(reg_)
    for node in check_:
        node_list.append(node)
        map_new[(node[0], node[1])] = 1
        if node[0] == c[0] and node[1] == c[1]:
            map_new[(node[0], node[1])] = 0
    final = intersection(node_list, obstacle)
    for item in final:
        map_new[(item[0], item[1])] = 0

    return map_new, node_list, c, final, ob_cur


def prep_a_star(startx, starty, e):
    print('Processing nodes')
    start_time = time.time()
    start = (startx, starty)
    for i in map_:
        grid, reg_list, center_, final, other = image_c(i, e)
    end_time = time.time()
    print('Time:', end_time - start_time)

    goal = center_
    map_new = grid
    valid = reg_list
    #print(valid)
    obs = final
    invalid = other
    return map_new, start, goal, obs, valid, invalid


def newMap(grid, obs, valid, invalid):
    print('Processing New Map')
    start_time = time.time()

    b = np.zeros((grid.shape[0], grid.shape[1]), np.uint8)

    for i in range(0, b.shape[0]):
        for j in range(0, b.shape[1]):
            node = (i, j)
            if node in valid:
                b[node] = 255
            elif node in obs:
                b[node] = 0
            elif node in invalid:
                b[node] = 0
            else:
                b[node] = 0

    end_time = time.time()
    print('Time:', end_time - start_time)
    print(b)
    print('Processing Complete')
    return b


def newregion(grid, valid):
    print('Processing New Map')
    start_time = time.time()

    b = np.zeros((grid.shape[0], grid.shape[1]), np.uint8)

    for i in range(0, b.shape[0]):
        for j in range(0, b.shape[1]):
            node = (i, j)
            if node in valid:
                b[node] = 0
            else:
                b[node] = 255

    end_time = time.time()
    print('Time:', end_time - start_time)
    print(b)
    print('Processing Complete')
    return b


def sub_region(valid, n):
    inc = int(abs((len(valid)) // n))
    #print(inc)
    dic_n = {}
    st = 0
    for i in range(0, n, 1):
        dic_n[i] = list(valid[st:st+inc])
        st = st+inc

    return dic_n


def main():
    startx = int(input())
    starty = int(input())
    room = int(input())
    maze, start, end, obs, valid, invalid = prep_a_star(startx, starty, room)
    j = newMap(maze, obs, valid, invalid)
    plt.imshow(j, cmap="gray")
    plt.axis('off')
    plt.savefig("test_fff_out.png", bbox_inches='tight')


if __name__ == "__main__":
    main()
