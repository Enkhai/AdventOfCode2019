import sys
from shapely.geometry import LineString

wires = []
with open("inputs/advent3input.txt", "r") as file:
    for line in file.readlines():
        wires.append(line.split(","))


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def wire_path(wire):
    path = []
    x_y = [0, 0]
    for direction in wire:
        increment = int(direction[1:])
        if direction[0] == 'R':
            x_y[0] += increment
        elif direction[0] == 'L':
            x_y[0] -= increment
        elif direction[0] == 'U':
            x_y[1] += increment
        elif direction[0] == 'D':
            x_y[1] -= increment
        else:
            print("Wrong direction input!")
            sys.exit()
        path.append(x_y.copy())

    return path


def find_all_intersection_distances(data):
    wire_paths = []
    for wire in data:
        wire_paths.append(wire_path(wire))

    intersection_distances = []

    for i in range(len(wire_paths)):
        for j in range(i + 1, len(wire_paths)):
            path_i = wire_paths[i]
            path_j = wire_paths[j]

            for i_point_idx in range(len(path_i) - 1):
                for j_point_idx in range(len(path_j) - 1):
                    intersection = LineString([path_i[i_point_idx], path_i[i_point_idx + 1]]) \
                        .intersection(LineString([path_j[j_point_idx], path_j[j_point_idx + 1]]))
                    if not intersection.is_empty:
                        intersection_distances.append(manhattan_distance([intersection.x, intersection.y], [0, 0]))

    return intersection_distances


def find_closest_intersection_distance(data):
    intersection_distances = find_all_intersection_distances(data)
    minimum_distance = sys.maxsize
    for distance in intersection_distances:
        minimum_distance = distance if distance < minimum_distance else minimum_distance
    return minimum_distance


if __name__ == '__main__':
    print(find_closest_intersection_distance(wires))
