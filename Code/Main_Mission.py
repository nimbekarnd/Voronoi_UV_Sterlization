import sys
import try_img as step1
import try_import as step2
import try_err as step3
import areaalgo as Area
import matplotlib.pyplot as plt
import time



def select_room(w, h, n):
    # generate_map(w, h)
    if n == 1:
        maze, start, end, obs, valid, invalid = step1.prep_a_star(0, 0, n)
    elif n == 2:
        maze, start, end, obs, valid, invalid = step1.prep_a_star((w//2), 0, n)
    elif n == 3:
        maze, start, end, obs, valid, invalid = step1.prep_a_star(w//2, h//2, n)
    elif n == 4:
        maze, start, end, obs, valid, invalid = step1.prep_a_star(0, h//2, n)
    j = step1.newMap(maze, obs, valid, invalid)
    plt.imshow(j, cmap="gray")
    plt.axis('off')
    plt.savefig("test_fff_out.png", bbox_inches='tight')
    return maze, obs, valid, invalid


def select_method(w, h, valid, subdivide, room,  state):
    if state == 'standard':
        case = step1.sub_region(valid, subdivide)
    elif state == 'voronoi':
        case = step2.processing_voronoi(w, h, room, subdivide)
    #print('Case:', case)
    return case


def for_now(var, n):
    node_v = var.get(n)
    return node_v


def main():
    maze, obs, valid_nodes, invalid = select_room(w, h, room)
    a = Area.Area((8, 8), (w // 2, h // 2))
    subdivide = a.compare()
    dict_final = select_method(100, 100, valid_nodes, subdivide, room, 'standard')

    # print(dict_final)
    # valid_v = for_now(dict_final, 0)
    # print(valid_v)
    path_dict = {}
    for i in range(0, subdivide):
        valid_points = dict_final.get(i)
        # valid_v = for_now(dict_final, i)
        #print('valid', len(valid_points))
        #print(valid_points[0][1])

        # print(valid_points)
        l = step1.newregion(maze, valid_points)
        plt.imshow(l, cmap="gray")
        plt.axis('off')
        plt.savefig("out_room_reg%d.png" % i, bbox_inches='tight')
        path = step3.rep(valid_points[0][0], valid_points[0][1])
        #print('path',len(path))

        list_cover = []
        for elem in path:
            for node in valid_points:
                if elem == node:
                    list_cover.append(elem)
        path_dict[i] = list_cover
        # print(list_cover)
        print('Processing path visualization...')
        x_value = []
        y_value = []

        for i in range(len(list_cover) - 1):
            x1, y1 = list_cover[i][0], list_cover[i][1]
            x_value.append(y1)
            y_value.append(x1)
            plt.plot(x_value, y_value)
        

        print('Processing Completed...')
        #plt.scatter(*zip(*list_cover))
        plt.savefig("out_%d.png"%i)
        plt.show()
        coverage_percentage = (len(list_cover)//len(valid_points))*100
        print("coverage percentage:", coverage_percentage)
    return path_dict

if __name__ == "__main__":
    w = int(input())
    h = int(input())
    room = int(input())
    path_dict = main()
    # print(path_dict)
    
sys.exit()
