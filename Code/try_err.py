import numpy as np
import sys
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import time

sys.setrecursionlimit(100000)

image = Image.open('/home/ndnupur/Desktop/voronoi/Code/images/test_fff.png')
array = np.asarray(image)
map_array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)

map_ = np.zeros((map_array.shape[0] //2 , map_array.shape[1] // 2), dtype=int)
grid_size = np.multiply((map_array.shape[0])//2, (map_array.shape[1])//2)




route = []
par_ = []  # edge
walk = []  # path
par_child = {}
direction = [0, 0, 0, 1, 1]
path_status = [0, 1]


def count(node):
    counter = {}
    for node in par_:
        if node in counter:
            counter[node] += 1
        else:
            counter[node] = 1
    count = counter.get(node)
    return count


def rep(startx, starty):
    start = (startx, starty)
    par_.append(start)
    start_time = time.time()
    for i in range(grid_size):
        current = par_[-1]
        tree(current)
        i = i + 1
    end_time = time.time()

    for j in range(len(par_) - 1):

        dis = abs(par_[j][0] - par_[j+1][0]) + abs(par_[j][1] - par_[j+1][1])
        if dis == 0:
            pass
        elif dis == 1:
            walk.append(go_ahead(par_[j], par_[j+1]))
        elif dis == 2:
            mid = mid_node(par_[j], par_[j+1])
            walk.append(go_ahead(par_[j], mid))
            walk.append(go_ahead(mid, par_[j+1]))
    print('Time:', end_time - start_time)
    return par_


def mid_node(curr, next_):
    curr_n, next_n = set(), set()
    for a, b in route:
        if a == curr:
            curr_n.add(b)
        if b == curr:
            curr_n.add(a)
        if a == next_:
            next_n.add(b)
        if b == next_:
            next_n.add(a)
    inter = curr_n.intersection(next_n)

    if len(inter) == 0:
        sys.exit()
    elif len(inter) == 1:
        return list(inter)[0]
    else:
        sys.exit()


def get_dir(curr, next_):
    if curr[0] < next_[0] and curr[1] == next_[1]:
        return'South'
    elif curr[0] == next_[0] and curr[1] < next_[1]:
        return'East'
    elif curr[0] > next_[0] and curr[1] == next_[1]:
        return'North'
    elif curr[0] == next_[0] and curr[1] > next_[1]:
        return'West'
    else:
        sys.exit()


def go_ahead(curr, next_):
    dir_ = get_dir(curr, next_)
    # move east
    if dir_ == 'East':
        curr = get_sub_node(curr, 'SE')
        next_ = get_sub_node(next_, 'SW')
    # move west
    elif dir_ == 'West':
        curr = get_sub_node(curr, 'NW')
        next_ = get_sub_node(next_, 'NE')
    # move south
    elif dir_ == 'South':
        curr = get_sub_node(curr, 'SW')
        next_ = get_sub_node(next_, 'NW')
    # move north
    elif dir_ == 'North':
        curr = get_sub_node(curr, 'NE')
        next_ = get_sub_node(next_, 'SE')
    else:
        sys.exit('move direction error...')
    return [curr, next_]


def get_sub_node(node, dir_):
    if dir_ == 'SE':
        return [2*node[0]+1, 2*node[1]+1]
    elif dir_ == 'SW':
        return [2*node[0]+1, 2*node[1]]
    elif dir_ == 'NE':
        return [2*node[0], 2*node[1]+1]
    elif dir_ == 'NW':
        return [2*node[0], 2*node[1]]
    else:
        sys.exit('get_sub_node: sub-node direction error.')


def tree(curr):
    order = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    map_[(curr[0], curr[1])] += 1
    neigh = []
    for step in order:
        n_i, n_j = curr[0] + step[0], curr[1] + step[1]
        neigh.append((n_i, n_j))

    par_child[curr] = neigh
    next_node = par_child.get(curr)

    set_path = path_status.index(1)

    counter = True

    # onwards journey

    S = bool(0 <= (next_node[0][0]) < map_.shape[0] and 0 <= (next_node[0][1]) < map_.shape[1])  # South neighbour
    E = bool(0 <= (next_node[1][0]) < map_.shape[0] and 0 <= (next_node[1][1]) < map_.shape[1])  # East neighbour
    N = bool(0 <= (next_node[2][0]) < map_.shape[0] and 0 <= (next_node[2][1]) < map_.shape[1])  # North neighbour
    W = bool(0 <= (next_node[3][0]) < map_.shape[0] and 0 <= (next_node[3][1]) < map_.shape[1])  # West neighbour

    all_s = (np.logical_and(S, counter) and next_node[0] not in par_)
    all_e = (np.logical_and(E, counter) and next_node[1] not in par_)
    all_n = (np.logical_and(N, counter) and next_node[2] not in par_)
    all_w = (np.logical_and(W, counter) and next_node[3] not in par_)

    # return journey

    set_direction = direction.index(1)

    if set_path == 1:
        if set_direction == 0 or set_direction == 3:
            if all_s:
                print('reached South')
                par_.append(next_node[0])
                route.append((curr, next_node[0]))
                direction[0] = 1
                direction[1] = 0
                direction[2] = 0
                direction[3] = 0
                counter = False
            elif all_e:
                print('reached East')
                par_.append(next_node[1])
                route.append((curr, next_node[1]))
                direction[0] = 0
                direction[1] = 1
                direction[2] = 0
                direction[3] = 0
                counter = False
            elif all_n:
                print('reached North')
                par_.append(next_node[2])
                route.append((curr, next_node[2]))
                direction[0] = 0
                direction[1] = 0
                direction[2] = 1
                direction[3] = 0
                counter = False
            elif all_w:
                print('reached West')
                par_.append(next_node[3])
                route.append((curr, next_node[3]))
                direction[0] = 0
                direction[1] = 0
                direction[2] = 0
                direction[3] = 1
                counter = False
            else:
                print('None, South, West set but no neighbour available')
                path_status[0] = 1
                path_status[1] = 0
                direction[0] = 0
                direction[1] = 0
                direction[2] = 0
                direction[3] = 0
                direction[4] = 1
        elif set_direction == 1:
            if all_e:
                print('reached East')
                par_.append(next_node[1])
                route.append((curr, next_node[1]))
                direction[0] = 0
                direction[1] = 1
                direction[2] = 0
                direction[3] = 0
                counter = False
            elif all_s:
                print('reached South')
                par_.append(next_node[0])
                route.append((curr, next_node[0]))
                direction[0] = 1
                direction[1] = 0
                direction[2] = 0
                direction[3] = 0
                counter = False
            elif all_n:
                print('reached North')
                par_.append(next_node[2])
                route.append((curr, next_node[2]))
                direction[0] = 0
                direction[1] = 0
                direction[2] = 1
                direction[3] = 0
                counter = False
            elif all_w:
                print('reached West')
                par_.append(next_node[3])
                route.append((curr, next_node[3]))
                direction[0] = 0
                direction[1] = 0
                direction[2] = 0
                direction[3] = 1
                counter = False
            else:
                print('East set but no neighbour available')
                path_status[0] = 1
                path_status[1] = 0
                direction[0] = 0
                direction[1] = 0
                direction[2] = 0
                direction[3] = 0
                direction[4] = 1
        elif set_direction == 2:
            if all_n:
                print('reached North')
                par_.append(next_node[2])
                route.append((curr, next_node[2]))
                direction[0] = 0
                direction[1] = 0
                direction[2] = 1
                direction[3] = 0
                counter = False
            elif all_s:
                print('reached South')
                par_.append(next_node[0])
                route.append((curr, next_node[0]))
                direction[0] = 1
                direction[1] = 0
                direction[2] = 0
                direction[3] = 0
                counter = False
            elif all_e:
                print('reached East')
                par_.append(next_node[1])
                route.append((curr, next_node[1]))
                direction[0] = 0
                direction[1] = 1
                direction[2] = 0
                direction[3] = 0
                counter = False
            elif all_w:
                print('reached West')
                par_.append(next_node[3])
                route.append((curr, next_node[3]))
                direction[0] = 0
                direction[1] = 0
                direction[2] = 0
                direction[3] = 1
                counter = False
            else:
                print('North set but no neighbour available')
                path_status[0] = 1
                path_status[1] = 0
                direction[0] = 0
                direction[1] = 0
                direction[2] = 0
                direction[3] = 0
                direction[4] = 1
    return map_


#
def main():
    start = rep(0, 0)
    #print(par_)
    print('processing')
    x_value = []
    y_value = []
    for i in range(len(par_)-1):
        x1,y1 = par_[i][0], par_[i][1]
        x_value.append(x1)
        y_value.append(y1)

        plt.plot(x_value, y_value)
    print('processing completed')

    plt.gca().invert_yaxis()

    #plt.scatter(*zip(*par_))
    plt.show()


if __name__ == "__main__":
    main()
